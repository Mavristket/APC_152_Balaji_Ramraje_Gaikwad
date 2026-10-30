"""
Sorting Algorithm Race
----------------------
Compare six sorting methods on different input patterns.

Buttons:
1. Make Graph: benchmark generated datasets and save results.csv,
   benchmark_report.txt, and sorting_race.png.
2. Sort with selected: sort the array entered by the user.
3. Compare all & save report: benchmark every eligible algorithm on
   the user's array and save user_array_report.txt.
"""

import queue
import random
import statistics
import threading
import time
import tkinter as tk
from tkinter import scrolledtext, ttk

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


# --------------------------- Project settings ---------------------------

SIZES = [100, 500, 1_000, 2_000, 5_000]
SHAPES = ["random", "already sorted", "reversed", "nearly sorted", "many duplicates"]
REPETITIONS = 5
SEED = 42
MAX_QUADRATIC_SIZE = 5_000

# Keep the same color for each algorithm in every graph panel.
COLORS = {
    "bubble": "#C76D52",
    "insertion": "#D49A32",
    "merge": "#2D8069",
    "quick": "#4C75A5",
    "heap": "#8B6BA8",
    "Python sorted": "#687A76",
}

# The algorithms used by both benchmarking features.
ALGORITHMS = {
    "bubble": None,       # Filled in after the sorting functions are defined.
    "insertion": None,
    "merge": None,
    "quick": None,
    "heap": None,
    "Python sorted": sorted,
}


# --------------------------- Sorting algorithms ---------------------------

def bubble_sort(values):
    """Bubble sort: repeatedly move larger neighboring values to the right."""
    result = values.copy()

    for end in range(len(result) - 1, 0, -1):
        swapped = False

        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True

        # If no values were swapped, the list is already sorted.
        if not swapped:
            break

    return result


def insertion_sort(values):
    """Insertion sort: insert each value into its correct place in the left side."""
    result = values.copy()

    for index in range(1, len(result)):
        value = result[index]
        position = index - 1

        # Shift larger values one position to the right.
        while position >= 0 and result[position] > value:
            result[position + 1] = result[position]
            position -= 1

        result[position + 1] = value

    return result


def merge_sort(values):
    """Bottom-up merge sort: merge sorted groups, doubling group size each pass."""
    source = values.copy()
    destination = source.copy()
    width = 1

    while width < len(source):
        # Merge two neighboring groups of size 'width'.
        for start in range(0, len(source), 2 * width):
            middle = min(start + width, len(source))
            end = min(start + 2 * width, len(source))
            left = start
            right = middle

            for output_index in range(start, end):
                # Take the smaller available value from the two groups.
                if left < middle and (
                    right >= end or source[left] <= source[right]
                ):
                    destination[output_index] = source[left]
                    left += 1
                else:
                    destination[output_index] = source[right]
                    right += 1

        # Swap source and destination for the next merging pass.
        source, destination = destination, source
        width *= 2

    return source


def quick_sort(values):
    """Iterative quick sort with a randomized pivot and duplicate handling."""
    result = values.copy()

    if len(result) < 2:
        return result

    rng = random.Random(SEED)
    pending_ranges = [(0, len(result) - 1)]

    # A stack avoids recursive calls and possible recursion-depth problems.
    while pending_ranges:
        low, high = pending_ranges.pop()

        if low >= high:
            continue

        # A random pivot helps avoid poor performance on sorted input.
        pivot = result[rng.randint(low, high)]
        lower = current = low
        upper = high

        # Partition into values smaller than, equal to, and greater than pivot.
        while current <= upper:
            if result[current] < pivot:
                result[lower], result[current] = result[current], result[lower]
                lower += 1
                current += 1
            elif result[current] > pivot:
                result[current], result[upper] = result[upper], result[current]
                upper -= 1
            else:
                current += 1

        # Sort the parts to the left and right of the equal-to-pivot section.
        if low < lower - 1:
            pending_ranges.append((low, lower - 1))
        if upper + 1 < high:
            pending_ranges.append((upper + 1, high))

    return result


def heap_sort(values):
    """Heap sort: build a max heap, then repeatedly move its maximum to the end."""
    result = values.copy()

    def sift_down(root, heap_size):
        """Move a parent down until it is larger than its children."""
        while 2 * root + 1 < heap_size:
            child = 2 * root + 1
            larger_child = child

            if child + 1 < heap_size and result[child + 1] > result[child]:
                larger_child = child + 1

            if result[root] >= result[larger_child]:
                return

            result[root], result[larger_child] = result[larger_child], result[root]
            root = larger_child

    # Build a max heap from the unsorted list.
    for root in range(len(result) // 2 - 1, -1, -1):
        sift_down(root, len(result))

    # Put the largest remaining value at the end on each pass.
    for end in range(len(result) - 1, 0, -1):
        result[0], result[end] = result[end], result[0]
        sift_down(0, end)

    return result


# Fill the algorithm dictionary now that all functions exist.
ALGORITHMS.update({
    "bubble": bubble_sort,
    "insertion": insertion_sort,
    "merge": merge_sort,
    "quick": quick_sort,
    "heap": heap_sort,
})


# --------------------------- Test data generation ---------------------------

def generate_data(seed=SEED):
    """Create reproducible test lists for each input shape and size."""
    rng = random.Random(seed)
    datasets = {shape: {} for shape in SHAPES}

    for size in SIZES:
        # Start with random integers and use them to make several patterns.
        random_values = [rng.randint(0, size * 10) for _ in range(size)]
        sorted_values = sorted(random_values)

        datasets["random"][size] = random_values
        datasets["already sorted"][size] = sorted_values
        datasets["reversed"][size] = sorted(random_values, reverse=True)

        # Nearly sorted: swap about 1% of the values in the sorted list.
        nearly_sorted = sorted_values.copy()
        swap_count = max(1, round(size * 0.01))

        for _ in range(swap_count):
            left, right = rng.sample(range(size), 2)
            nearly_sorted[left], nearly_sorted[right] = (
                nearly_sorted[right], nearly_sorted[left]
            )

        datasets["nearly sorted"][size] = nearly_sorted

        # Duplicate-heavy: draw values from a small range.
        duplicate_limit = max(1, size // 20)
        datasets["many duplicates"][size] = [
            rng.randint(0, duplicate_limit) for _ in range(size)
        ]

    return datasets


def parse_integer_array(text):
    """Convert comma-separated text such as '8, 3, 5' into a list of integers."""
    cleaned = text.strip()

    # Square brackets are optional.
    if cleaned.startswith("[") and cleaned.endswith("]"):
        cleaned = cleaned[1:-1].strip()

    if not cleaned:
        raise ValueError("Enter at least one integer.")

    tokens = cleaned.split(",")

    if any(not token.strip() for token in tokens):
        raise ValueError("Separate integers with commas; do not leave empty items.")

    try:
        return [int(token.strip()) for token in tokens]
    except ValueError as error:
        raise ValueError("Enter integers only, separated by commas.") from error


# --------------------------- Benchmarking ---------------------------

def sort_user_array(values, algorithm_name):
    """Sort one user list, time it, and check correctness and input preservation."""
    if algorithm_name not in ALGORITHMS:
        raise ValueError(f"Unknown sorting algorithm: {algorithm_name}")

    if algorithm_name in {"bubble", "insertion"} and len(values) > MAX_QUADRATIC_SIZE:
        raise ValueError(
            f"{algorithm_name} is limited to {MAX_QUADRATIC_SIZE} values "
            "to avoid a long run."
        )

    original = values.copy()
    start_time = time.perf_counter()
    result = ALGORITHMS[algorithm_name](values)
    elapsed = time.perf_counter() - start_time

    # Every function must return a sorted copy without changing the input.
    if result != sorted(original) or values != original or result is values:
        raise ValueError(f"{algorithm_name} failed the sorting or input-preservation check")

    return result, elapsed


def benchmark(datasets, repetitions=REPETITIONS, progress_callback=None):
    """Run every eligible algorithm several times and store median timings."""
    test_count = sum(
        1
        for shape_data in datasets.values()
        for size in shape_data
        for name in ALGORITHMS
        if not (name in {"bubble", "insertion"} and size > MAX_QUADRATIC_SIZE)
    )

    completed = 0
    results = []

    for shape, shape_data in datasets.items():
        for size, original in shape_data.items():
            expected = sorted(original)

            for algorithm_name, algorithm in ALGORITHMS.items():
                # Avoid very long quadratic runs for sizes above the limit.
                if algorithm_name in {"bubble", "insertion"} and size > MAX_QUADRATIC_SIZE:
                    continue

                completed += 1
                message = f"[{completed}/{test_count}] {algorithm_name} | {shape} | n={size}"

                if progress_callback is None:
                    print(message, flush=True)
                else:
                    progress_callback(completed, test_count, message)

                run_times = []

                for _ in range(repetitions):
                    run_input = original.copy()
                    input_before_run = run_input.copy()

                    start_time = time.perf_counter()
                    output = algorithm(run_input)
                    elapsed = time.perf_counter() - start_time

                    # Verify the answer and make sure the original input was not changed.
                    if output != expected:
                        raise ValueError(
                            f"{algorithm_name} returned an incorrect result "
                            f"for {shape}, size {size}"
                        )
                    if output is run_input or run_input != input_before_run:
                        raise ValueError(
                            f"{algorithm_name} did not preserve its input and "
                            "return a new list"
                        )

                    run_times.append(elapsed)

                results.append({
                    "algorithm": algorithm_name,
                    "shape": shape,
                    "size": size,
                    "time_seconds": statistics.median(run_times),
                })

    return pd.DataFrame(
        results, columns=["algorithm", "shape", "size", "time_seconds"]
    )


# --------------------------- Graph and reports ---------------------------

def plot_results(results, output_path="sorting_race.png", show=True,
                 figsize=(17, 5.2)):
    """Plot the benchmark results using log scales and a clear shared legend."""
    figure, axes = plt.subplots(
        1, len(SHAPES), figsize=figsize, facecolor="#F4F7F5"
    )

    # Make sure 'axes' is iterable even if only one panel is ever requested.
    axes = np.atleast_1d(axes)

    for axis, shape in zip(axes, SHAPES):
        shape_results = results[results["shape"] == shape]

        for algorithm, measurements in shape_results.groupby("algorithm", sort=False):
            measurements = measurements.sort_values("size")
            axis.loglog(
                measurements["size"],
                measurements["time_seconds"],
                marker="o",
                markersize=4,
                linewidth=1.8,
                color=COLORS.get(algorithm, "#52645A"),
                label=algorithm,
            )

        axis.set_title(shape.title(), fontsize=11, fontweight="semibold", pad=10)
        axis.set_xlabel("Input size (n)")
        axis.set_ylabel("Median time (seconds)")
        axis.set_facecolor("#FFFFFF")
        axis.set_axisbelow(True)
        axis.grid(True, which="major", color="#DCE5DF", linewidth=0.8)
        axis.grid(True, which="minor", color="#EDF1EE", linestyle=":", linewidth=0.5)
        axis.tick_params(colors="#52645A", labelsize=8)

        for spine in axis.spines.values():
            spine.set_color("#DCE5DF")

    # One legend for all panels, instead of repeating it five times.
    handles, labels = axes[0].get_legend_handles_labels()
    figure.legend(
        handles, labels,
        loc="upper center",
        bbox_to_anchor=(0.5, 0.94),
        ncol=len(labels),
        frameon=False,
        fontsize=9,
    )

    # Reserve enough space above the graph. This prevents the title being
    # cut off in the full-screen window and when the image is saved.
    figure.suptitle(
        "Sorting Performance Across Input Patterns",
        y=0.995,
        fontsize=16,
        fontweight="bold",
        color="#24332B",
    )
    figure.tight_layout(rect=(0, 0, 1, 0.84), pad=1.6, w_pad=1.4)

    if output_path:
        figure.savefig(output_path, dpi=160, bbox_inches="tight", pad_inches=0.25)
        print(f"Saved plot to {output_path}")

    if show:
        plt.show()

    return figure


def calculate_exponent(group):
    """Estimate the growth exponent from a straight line on a log-log graph."""
    x = np.log(group["size"].to_numpy(dtype=float))
    y = np.log(group["time_seconds"].to_numpy(dtype=float))
    exponent, _ = np.polyfit(x, y, 1)
    return exponent


def fit_exponents(results):
    """Print estimated empirical growth rates for each algorithm and input shape."""
    print("\nEmpirical exponents (time approximately proportional to n^exponent):")

    for (algorithm, shape), group in results.groupby(["algorithm", "shape"]):
        if len(group) >= 2:
            exponent = calculate_exponent(group)
            print(f"{algorithm} on {shape}: n^{exponent:.2f}")


def format_benchmark_report(results):
    """Create a readable report with growth estimates and fastest algorithms."""
    report_lines = [
        "SORTING ALGORITHM RACE: BENCHMARK REPORT",
        "=" * 43,
        f"Random seed: {SEED}",
        f"Input sizes: {', '.join(map(str, SIZES))}",
        f"Input shapes: {', '.join(SHAPES)}",
        f"Timing: median of {REPETITIONS} runs; time.perf_counter()",
        "Correctness: every output compared with Python sorted(input)",
        f"Bubble and insertion sort are skipped above n={MAX_QUADRATIC_SIZE}.",
        "",
        "EMPIRICAL GROWTH EXPONENTS",
        "Time is approximately proportional to n^exponent.",
    ]

    for (algorithm, shape), group in results.groupby(["algorithm", "shape"]):
        if len(group) >= 2:
            report_lines.append(
                f"{algorithm} on {shape}: n^{calculate_exponent(group):.2f}"
            )

    largest_size = int(results["size"].max())
    report_lines.extend([
        "",
        f"RANKINGS AT LARGEST SIZE (n={largest_size})",
        "Lower median time is faster.",
    ])

    for shape in SHAPES:
        ranking = results[
            (results["shape"] == shape) & (results["size"] == largest_size)
        ].sort_values("time_seconds")

        report_lines.extend(["", f"{shape.title()}:"])
        for rank, row in enumerate(ranking.itertuples(index=False), start=1):
            report_lines.append(
                f"{rank}. {row.algorithm}: {row.time_seconds:.8f} seconds"
            )

    report_lines.extend([
        "",
        f"Detailed measurements are in results.csv ({len(results)} rows).",
        "The corresponding log-log plot is sorting_race.png.",
    ])
    return "\n".join(report_lines)


def compare_user_array(values, repetitions=REPETITIONS, progress_callback=None):
    """Benchmark all eligible algorithms on a user list and rank the results."""
    results = benchmark(
        {"user input": {len(values): values}},
        repetitions=repetitions,
        progress_callback=progress_callback,
    ).sort_values("time_seconds")

    report_lines = [
        "SORTING REPORT: USER-PROVIDED ARRAY",
        "=" * 42,
        f"Input values ({len(values)}): {values}",
        f"Sorted result: {sorted(values)}",
        f"Timing: median of {repetitions} runs per algorithm",
        "",
        "Rank | Algorithm | Median time (seconds)",
        "-" * 42,
    ]

    for rank, row in enumerate(results.itertuples(index=False), start=1):
        report_lines.append(
            f"{rank:>4} | {row.algorithm} | {row.time_seconds:.8f}"
        )

    if len(values) > MAX_QUADRATIC_SIZE:
        report_lines.extend([
            "",
            f"Bubble and insertion sort were skipped because this input "
            f"exceeds {MAX_QUADRATIC_SIZE} values.",
        ])

    report_lines.extend([
        "",
        "All reported algorithms were checked against Python's sorted() result.",
    ])
    return results, "\n".join(report_lines)


# --------------------------- Tkinter application ---------------------------

def create_gui():
    """Build the window, connect buttons, and show benchmark progress and charts."""
    root = tk.Tk()
    root.title("Sorting Algorithm Race")
    root.geometry("1280x820")
    root.minsize(900, 600)
    root.configure(background="#F2F5F1")

    style = ttk.Style(root)
    if "clam" in style.theme_names():
        style.theme_use("clam")

    style.configure("TFrame", background="#F2F5F1")
    style.configure("TLabel", background="#F2F5F1", foreground="#24332B")
    style.configure("Header.TLabel", font=("Segoe UI", 22, "bold"), foreground="#173B2B")
    style.configure("Subtitle.TLabel", font=("Segoe UI", 10), foreground="#52645A")
    style.configure("Primary.TButton", padding=(14, 8), font=("Segoe UI", 10, "bold"))
    style.configure("TLabelframe", background="#F2F5F1")
    style.configure("TLabelframe.Label", background="#F2F5F1", foreground="#173B2B")

    root.columnconfigure(0, weight=1)
    root.rowconfigure(3, weight=1)

    # Main heading and short explanation.
    heading = ttk.Frame(root, padding=(20, 18, 20, 10))
    heading.grid(row=0, column=0, sticky="ew")
    ttk.Label(heading, text="Sorting Algorithm Race", style="Header.TLabel").pack(anchor="w")
    ttk.Label(
        heading,
        text=("Compare random, sorted, reversed, nearly sorted, and duplicate-heavy "
              "data (n=100 to 5,000). You can also enter your own array below."),
        style="Subtitle.TLabel",
    ).pack(anchor="w", pady=(3, 0))

    # Top row: graph button, full-screen button, status, and progress bar.
    controls = ttk.Frame(root, padding=(20, 8, 20, 14))
    controls.grid(row=1, column=0, sticky="ew")
    controls.columnconfigure(3, weight=1)

    progress_value = tk.IntVar(value=0)
    status_text = tk.StringVar(value="Ready")
    events = queue.Queue()

    graph_button = ttk.Button(controls, text="Make Graph", style="Primary.TButton")
    graph_button.grid(row=0, column=0, padx=(0, 14))

    fullscreen_button = ttk.Button(controls, text="Full-screen chart", state="disabled")
    fullscreen_button.grid(row=0, column=1, padx=(0, 12))

    ttk.Label(controls, textvariable=status_text).grid(row=0, column=2, padx=(0, 12))
    progress = ttk.Progressbar(
        controls, variable=progress_value, maximum=1, mode="determinate"
    )
    progress.grid(row=0, column=3, sticky="ew")

    # Input area: one selected algorithm or a comparison of all algorithms.
    input_panel = ttk.Labelframe(
        root, text="Your input: compare algorithms on this array", padding=(12, 8)
    )
    input_panel.grid(row=2, column=0, sticky="ew", padx=20, pady=(0, 12))
    input_panel.columnconfigure(1, weight=1)

    input_text = tk.StringVar(value="8, 3, 5, 1, 9")
    algorithm_choice = tk.StringVar(value="Python sorted")

    ttk.Label(input_panel, text="Your array (sample shown)").grid(
        row=0, column=0, padx=(0, 8), sticky="w"
    )
    input_entry = ttk.Entry(input_panel, textvariable=input_text)
    input_entry.grid(row=0, column=1, sticky="ew", padx=(0, 10))

    algorithm_picker = ttk.Combobox(
        input_panel,
        textvariable=algorithm_choice,
        values=tuple(ALGORITHMS.keys()),
        state="readonly",
        width=16,
    )
    algorithm_picker.grid(row=0, column=2, padx=(0, 8))

    sort_input_button = ttk.Button(input_panel, text="Sort with selected")
    sort_input_button.grid(row=0, column=3, padx=(0, 6))

    compare_button = ttk.Button(input_panel, text="Compare all & save report")
    compare_button.grid(row=0, column=4)

    ttk.Label(input_panel, text="Result / report").grid(
        row=1, column=0, sticky="nw", padx=(0, 8), pady=(8, 0)
    )
    input_result = scrolledtext.ScrolledText(
        input_panel, height=7, wrap="word", font=("Consolas", 9),
        background="#FFFFFF", foreground="#24332B", relief="flat",
        padx=8, pady=6, state="disabled",
    )
    input_result.grid(row=1, column=1, columnspan=4, sticky="ew", pady=(8, 0))

    # Bottom area: progress log on the left and chart on the right.
    content = ttk.Panedwindow(root, orient="horizontal")
    content.grid(row=3, column=0, sticky="nsew", padx=20, pady=(0, 20))

    log_panel = ttk.Labelframe(content, text="Progress and analysis", padding=8)
    plot_panel = ttk.Labelframe(content, text="Timing curves", padding=8)
    content.add(log_panel, weight=1)
    content.add(plot_panel, weight=3)

    log_panel.rowconfigure(0, weight=1)
    log_panel.columnconfigure(0, weight=1)

    log = scrolledtext.ScrolledText(
        log_panel, wrap="word", font=("Consolas", 9),
        background="#FFFFFF", foreground="#24332B", relief="flat",
        padx=10, pady=10, state="disabled",
    )
    log.grid(row=0, column=0, sticky="nsew")

    ttk.Label(
        plot_panel,
        text="Click Make Graph to compare sorting speeds.",
        style="Subtitle.TLabel",
    ).pack(expand=True)

    # These variables remember the most recent graph and benchmark data.
    current_figure = None
    current_results = None
    fullscreen_window = None
    fullscreen_figure = None

    def append_log(message):
        """Add one message to the read-only progress log."""
        log.configure(state="normal")
        log.insert("end", message.rstrip() + "\n")
        log.see("end")
        log.configure(state="disabled")

    def show_user_report(report):
        """Display a result or report in the user-input panel."""
        input_result.configure(state="normal")
        input_result.delete("1.0", "end")
        input_result.insert("end", report)
        input_result.configure(state="disabled")

    def set_action_buttons_enabled(enabled):
        """Disable action buttons during work so jobs do not overlap."""
        state = "normal" if enabled else "disabled"
        for button in (graph_button, sort_input_button, compare_button):
            button.configure(state=state)

    def sort_input_array():
        """Run the selected sorting algorithm on the entered array."""
        try:
            values = parse_integer_array(input_text.get())
            name = algorithm_choice.get()
            result, elapsed = sort_user_array(values, name)
            message = f"{name} | {elapsed:.8f} seconds\n{result}"
        except ValueError as error:
            message = f"Input error: {error}"

        show_user_report(message)

    def start_user_comparison():
        """Start a background job to compare algorithms on the user's array."""
        try:
            values = parse_integer_array(input_text.get())
        except ValueError as error:
            show_user_report(f"Input error: {error}")
            return

        set_action_buttons_enabled(False)
        progress.configure(maximum=1)
        progress_value.set(0)
        status_text.set("Comparing algorithms on your array...")

        def comparison_worker():
            """Do the time-consuming comparison away from the GUI thread."""
            try:
                _, report = compare_user_array(
                    values,
                    progress_callback=lambda done, total, message:
                        events.put(("user_progress", (done, total, message))),
                )
                with open("user_array_report.txt", "w", encoding="utf-8") as file:
                    file.write(report)
                events.put(("user_complete", report))
            except Exception as error:
                events.put(("user_error", f"{type(error).__name__}: {error}"))

        threading.Thread(target=comparison_worker, daemon=True).start()

    def run_benchmark_worker():
        """Benchmark generated datasets in a worker thread."""
        try:
            results = benchmark(
                generate_data(),
                progress_callback=lambda done, total, message:
                    events.put(("progress", (done, total, message))),
            )
            results.to_csv("results.csv", index=False)

            report = format_benchmark_report(results)
            with open("benchmark_report.txt", "w", encoding="utf-8") as file:
                file.write(report)

            events.put(("complete", (results, report)))
        except Exception as error:
            events.put(("error", f"{type(error).__name__}: {error}"))

    def display_chart(parent, figure):
        """Embed a Matplotlib figure and its navigation toolbar in a Tk window."""
        canvas = FigureCanvasTkAgg(figure, master=parent)
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, parent, pack_toolbar=False)
        toolbar.update()
        toolbar.pack(side="bottom", fill="x")
        canvas.get_tk_widget().pack(side="top", fill="both", expand=True)

    def close_fullscreen_chart():
        """Close the full-screen chart and release its figure."""
        nonlocal fullscreen_window, fullscreen_figure

        if fullscreen_figure is not None:
            plt.close(fullscreen_figure)
            fullscreen_figure = None

        if fullscreen_window is not None:
            fullscreen_window.destroy()
            fullscreen_window = None

    def show_fullscreen_chart():
        """Open the latest graph in a full-screen window with a safe title margin."""
        nonlocal fullscreen_window, fullscreen_figure

        if current_results is None:
            return

        if fullscreen_window is not None and fullscreen_window.winfo_exists():
            fullscreen_window.focus_force()
            return

        fullscreen_window = tk.Toplevel(root)
        fullscreen_window.title("Sorting Algorithm Race - Full-screen chart")
        fullscreen_window.attributes("-fullscreen", True)
        fullscreen_window.bind("<Escape>", lambda _event: close_fullscreen_chart())
        fullscreen_window.protocol("WM_DELETE_WINDOW", close_fullscreen_chart)

        ttk.Button(
            fullscreen_window,
            text="Exit full screen (Esc)",
            command=close_fullscreen_chart,
        ).pack(anchor="ne", padx=12, pady=8)

        # A taller figure plus the reserved top margin prevents the title
        # and legend from being clipped at the top of the full-screen window.
        fullscreen_figure = plot_results(
            current_results,
            output_path=None,
            show=False,
            figsize=(16, 8.5),
        )
        display_chart(fullscreen_window, fullscreen_figure)

    def poll_events():
        """Read worker messages and update Tk widgets on the main thread."""
        nonlocal current_figure, current_results

        try:
            while True:
                event_type, payload = events.get_nowait()

                if event_type in ("progress", "user_progress"):
                    done, total, message = payload
                    progress.configure(maximum=total)
                    progress_value.set(done)

                    if event_type == "progress":
                        status_text.set(f"Running {done} of {total}")
                    else:
                        status_text.set(f"Comparing your array: {done} of {total}")

                    append_log(message)

                elif event_type == "complete":
                    results, report = payload
                    current_results = results
                    append_log("Saved results to results.csv")
                    append_log(report)

                    # Remove the placeholder or previous chart before drawing a new one.
                    for child in plot_panel.winfo_children():
                        child.destroy()

                    if current_figure is not None:
                        plt.close(current_figure)

                    current_figure = plot_results(results, show=False)
                    display_chart(plot_panel, current_figure)
                    fullscreen_button.configure(state="normal")
                    status_text.set(
                        "Graph saved as sorting_race.png; results and report saved"
                    )
                    set_action_buttons_enabled(True)

                elif event_type == "error":
                    status_text.set("Benchmark failed")
                    append_log(f"Error: {payload}")
                    set_action_buttons_enabled(True)

                elif event_type == "user_complete":
                    show_user_report(str(payload))
                    status_text.set("Your report is saved as user_array_report.txt")
                    append_log("Saved complete custom-array report to user_array_report.txt")
                    set_action_buttons_enabled(True)

                elif event_type == "user_error":
                    status_text.set("Your array comparison failed")
                    show_user_report(f"Error: {payload}")
                    append_log(f"Custom-array comparison error: {payload}")
                    set_action_buttons_enabled(True)

        except queue.Empty:
            # An empty queue simply means there are no new messages right now.
            pass

        # Check the queue again after 100 milliseconds.
        root.after(100, poll_events)

    def make_graph():
        """Clear old log messages and start the generated-data benchmark."""
        set_action_buttons_enabled(False)
        status_text.set("Preparing graph...")
        progress.configure(maximum=1)
        progress_value.set(0)

        log.configure(state="normal")
        log.delete("1.0", "end")
        log.configure(state="disabled")
        append_log("Preparing deterministic test datasets...")

        threading.Thread(target=run_benchmark_worker, daemon=True).start()

    # Connect buttons and keyboard Enter to their functions.
    sort_input_button.configure(command=sort_input_array)
    compare_button.configure(command=start_user_comparison)
    fullscreen_button.configure(command=show_fullscreen_chart)
    graph_button.configure(command=make_graph)
    input_entry.bind("<Return>", lambda _event: sort_input_array())

    root.after(100, poll_events)
    root.mainloop()


def main():
    """Start the graphical application."""
    create_gui()


if __name__ == "__main__":
    main()
