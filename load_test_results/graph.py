import re
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

directory = "./"  # Replace with the actual directory path

requests_sec = []
labels = []

# Iterate over the files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        file_path = os.path.join(directory, filename)
        labels.append(os.path.splitext(filename)[0])

        with open(file_path, "r") as file:
            content = file.read()
            # Extract the Requests/sec value using regular expressions
            match = re.search(r"Requests/sec:\s+([\d.]+)", content)
            if match:
                requests_sec.append(float(match.group(1)))

# Sort the labels and requests_sec lists together based on the requests_sec values
labels, requests_sec = zip(*sorted(zip(labels, requests_sec), key=lambda x: x[1], reverse=True))

# Format the y-axis labels to display values in hundreds of thousands
formatter = FuncFormatter(lambda x, _: '{:,.0f}'.format(x / 1000))

# Plot the graph
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
bars = plt.bar(labels, requests_sec)
plt.xlabel("Subject")
plt.ylabel("Requests/sec (in hundreds of thousands)")
plt.title("Requests/sec Comparison")
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.gca().yaxis.set_major_formatter(formatter)  # Apply the formatter to the y-axis labels

# Display the actual values on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval, f'{yval:,.2f}', ha='center', va='bottom')

plt.tight_layout()  # Adjust the spacing of the graph elements
plt.savefig("requests_sec_graph.png")  # Save the graph as a PNG file