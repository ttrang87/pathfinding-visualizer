import { animateMaze, renderMaze } from "./RenderMaze.js";

document.getElementById('RandomMazeButton').addEventListener('click', async () => {
    const animate = document.getElementById('AnimateCheckbox').checked; // Check if animation is enabled

    const data = {
        rows: defaultrows,
        cols: defaultcols,
        start: [startCell.row, startCell.col],
        end: [endCell.row, endCell.col],
        animate: animate  
    };

    try {
        const response = await axios.post('/maze/random', data);
        const { maze, steps } = response.data;

        if (animate) {
            animateMaze(steps, defaultrows, defaultcols);
        } else {
            renderMaze(maze, defaultrows, defaultcols); 
        }
    } catch (error) {
        console.error('Error generating maze:', error);
    }
});


