import { statusCell } from "../StatusCell.js"
import {renderPath, resetCellColors, animateVisitedCells} from "./CellsColor.js"
import { updateInfor, scrollToBottom, showToast } from "./InformationPanel.js";


document.getElementById('DFSButton').addEventListener('click', async () => {
    resetCellColors();
    showToast('Depth-first Search is unweighted and does not guarantee the shortest path!');
    const maze = statusCell()


    const data = {
        maze: maze,
        start: [startCell.row, startCell.col],
        end: [endCell.row, endCell.col],

    };

    try {
        const response = await axios.post('/pathfinding/dfs', data);
        const { path, visited_cells, time } = response.data;
        updateInfor("DFS", visited_cells, time, path)
        scrollToBottom();
        await animateVisitedCells(visited_cells);

        // After visited cells are animated, render the path
        renderPath(path);
    } catch (error) {
        console.error('Error generating maze:', error);
    }
});

