import { animateMaze, renderMaze } from "./RenderMaze.js";
import { isRunning, setRunningState } from "../path_find/SharedFunction.js";
import { showToast } from "../path_find/InformationPanel.js";

document.getElementById('HorizontalMazeButton').addEventListener('click', async () => {
    if (isRunning) {
            showToast('An algorithm is already running. Please wait!');
            return; // Prevent starting a new algorithm
        }
    
    const animate = document.getElementById('AnimateCheckbox').checked; // Check if animation is enabled

    const data = {
        rows: defaultrows,
        cols: defaultcols,
        start: [startCell.row, startCell.col],
        end: [endCell.row, endCell.col],
        animate: animate  
    };

    try {
        setRunningState(true)
        const response = await axios.post('/maze/horizontal', data);
        const { maze, steps } = response.data;

        if (animate) {
            animateMaze(steps, defaultrows, defaultcols);
        } else {
            renderMaze(maze, defaultrows, defaultcols); 
        }
    } catch (error) {
        console.error('Error generating maze:', error);
    } finally {
        setRunningState(false)
    }
});


