import { statusCell } from "../StatusCell.js"
import {renderPath, resetCellColors, animateVisitedCells} from "./CellsColor.js"


document.getElementById('DFSButton').addEventListener('click', async () => {
    resetCellColors();
    const maze = statusCell()


    const data = {
        maze: maze,
        start: [startCell.row, startCell.col],
        end: [endCell.row, endCell.col],

    };

    try {
        const response = await axios.post('/pathfinding/dfs', data);
        const { path, visited_cells } = response.data;
        await animateVisitedCells(visited_cells);

        // After visited cells are animated, render the path
        renderPath(path);
    } catch (error) {
        console.error('Error generating maze:', error);
    }
});

