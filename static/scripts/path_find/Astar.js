import { statusCell } from "../StatusCell.js"
import {renderPath, resetCellColors, animateVisitedCells} from "./CellsColor.js"
import { updateInfor, scrollToBottom, showToast } from "./InformationPanel.js";


document.getElementById('AstarButton').addEventListener('click', async () => {
    resetCellColors();
    showToast('A* Search is weighted and guarantees the shortest path!');
    const maze = statusCell()


    const data = {
        maze: maze,
        start: [startCell.row, startCell.col],
        end: [endCell.row, endCell.col],

    };

    try {
        const response = await axios.post('/pathfinding/astar', data);
        const { path, visited_cells, time } = response.data;
        updateInfor("A*", visited_cells, time, path)
        scrollToBottom();
        await animateVisitedCells(visited_cells);
        renderPath(path);
    } catch (error) {
        console.error('Error generating maze:', error);
    }
});

