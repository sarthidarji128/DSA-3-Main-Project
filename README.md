# CampusNet Designer 🌐💻

> **Campus Wi-Fi Network Designer — Prim's MST** is an interactive, high-fidelity single-page web application designed to model, visualize, and optimize campus-wide cabling layouts using Prim's Minimum Spanning Tree (MST) algorithm.

**Created by:** **Sarthi Darji**

This tool is built specifically to bridge the gap between technical optimization and stakeholder decision-making, offering intuitive visual aids, step-by-step algorithm traversals, and executive cost-benefit reports.

---

## 🚀 Key Features

### 1. Concept Demonstration (MST vs. Shortest Path)
* **Redundancy Visualization**: A side-by-side interactive comparison demonstrating why a union of Dijkstra's shortest paths creates costly, redundant cycles (e.g., 10 units of cabling) whereas Prim's MST guarantees an optimal, acyclic tree layout (e.g., 6 units of cabling).
* **Key Insight**: Clearly explains that Dijkstra minimizes distance from a single source *independently*, while Prim's minimizes *total global cabling cost*.

### 2. Live Step-by-Step Prim's Simulator
* **Interactive Canvas**: Watch the MST construct itself in real-time on a 6-node campus network graph starting from the central **DataCenter**.
* **Visual Traversal**:
  * **Green solid lines**: Completed MST edges with cost.
  * **Amber dashed lines**: Candidate edges currently in the Priority Queue.
  * **Faint gray lines**: Unexplored connections.
* **Audit Logs**: A real-time, color-coded console-style log recording every algorithm decision (e.g., additions, skips, and initializations).
* **Live Min-Heap (Priority Queue)**: Displays the state of the active candidate edge pool so users can trace how the min-heap chooses the next cheapest connection.

### 3. Scalability & Performance Analysis
* **Complexity Breakdown**: Compares incremental/local updates ($O(k \log n)$) against full-graph recompute ($O((V+E) \log V)$).
* **Interactive Addition Simulator**: Allows users to input a custom building name and estimated connection cost to determine if an incremental update is safe or if a full recalculation is recommended to maintain global optimality.

### 4. Cost Optimization & Executive Report
* **Financial Impact**: Summarizes cabling costs, showing a massive **65% savings** (₹18K MST cost vs. ₹52K full-mesh baseline).
* **Structural Viability Checks**: Automatically validates the generated layout against key network integrity rules:
  * Connectivity (all nodes reachable)
  * Cycle-free topology
  * Global cost optimality
  * Correct edge count ($n - 1$ edges for $n$ nodes)
* **Print Ready**: Optimized print layout with a dedicated print button (`window.print()`) for offline reporting and presentations.

### 5. Stakeholder-Oriented Design
* **Visual Clarity**: Color-coded network node states (Blue for data centers/active root, Green for connected MST nodes, and Gray for pending).
* **Accessibility**: Clean, modern dark-themed dashboard with clean UI custom properties, tab-based navigation, responsive grid layouts, and user avatar headers.
* **Security Guardrails**: Mock authentication system supporting multiple roles (Admin, Engineer, Guest) and credential validations.

---

## 🛠️ Technology Stack

* **Frontend**: Vanilla HTML5, CSS3, JavaScript (ES6+).
* **Graphics**: HTML5 `Canvas` API for dynamic graph, line, and node rendering.
* **Zero Dependencies**: Pure client-side code requiring no build tools, bundlers, libraries, or external packages. Run it anywhere instantly.

---

## 📂 Project Structure

```bash
.
├── index.html       # Single-page app containing styles, markup, and logic
├── .gitignore       # Git configuration to ignore system files and environment configs
└── README.md        # This documentation
```

---

## 🚦 Quick Start

To view and interact with the **CampusNet Designer** application:

1. **Clone or Download** the repository to your local machine.
2. **Open `index.html`** in any modern web browser (Chrome, Firefox, Safari, Edge, etc.) directly.
3. **Log in** using any of the following demo credentials:
   * **Admin** (Full Access): `admin` / `wifi123`
   * **Engineer**: `engineer` / `campus2024`
   * **Guest** (Read Only): `guest` / `view123`

---

## 📡 Default Campus Graph Specifications

The default network model represents a standard collegiate campus structure:

| Node ID | Building Name | Description |
| :---: | :--- | :--- |
| **0** | `DataCenter` | Central network infrastructure / root node |
| **1** | `AdminBlock` | Administrative office complex |
| **2** | `Library` | Academic library and learning resource center |
| **3** | `EnggBlock` | Engineering and technical block |
| **4** | `HostelA` | Student residential area |
| **5** | `SportsComplex` | Athletic facilities and outdoor arenas |

### Predefined Network Connections (Edges)
* `DataCenter ↔ AdminBlock` (Weight: 4)
* `DataCenter ↔ Library` (Weight: 6)
* `AdminBlock ↔ Library` (Weight: 2)
* `AdminBlock ↔ EnggBlock` (Weight: 5)
* `Library ↔ EnggBlock` (Weight: 3)
* `Library ↔ HostelA` (Weight: 7)
* `EnggBlock ↔ HostelA` (Weight: 4)
* `EnggBlock ↔ SportsComplex` (Weight: 6)
* `HostelA ↔ SportsComplex` (Weight: 5)
* `DataCenter ↔ SportsComplex` (Weight: 10)
