import { statusCell } from "../StatusCell.js"
import {renderPath, resetCellColors, animateVisitedCells, isRunning, setRunningState} from "./SharedFunction.js"
import { updateInfor, scrollToBottom, showToast } from "./InformationPanel.js";

document.getElementById('BFSButton').addEventListener('click', async () => {
    if (isRunning) {
            showToast('An algorithm is already running. Please wait!');
            return; // Prevent starting a new algorithm
        }
    
    resetCellColors();
    showToast('Breath-first Search is unweighted and guarantees the shortest path!');
    const maze = statusCell()


    const data = {
        maze: maze,
        start: [startCell.row, startCell.col],
        end: [endCell.row, endCell.col],

    };

    try {
        setRunningState(true);
        const response = await axios.post('/pathfinding/bfs', data);
        const { path, visited_cells, time } = response.data;
        updateInfor("BFS", visited_cells, time, path);
        scrollToBottom();
        await animateVisitedCells(visited_cells);
        renderPath(path);
    } catch (error) {
        console.error('Error generating maze:', error);
    } finally {
        setRunningState(false); // Reset the flag after completion
    }
});
