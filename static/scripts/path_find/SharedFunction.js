export let isRunning = false;

export function setRunningState(state) {
    isRunning = state;
}

export function resetCellColors() {
    // Remove visited class and reset background color for visited cells
    document.querySelectorAll('.visited').forEach(cell => {
        cell.classList.remove('visited');
        cell.style.backgroundColor = '#e2f1f7';
        cell.style.transition = '';
    });

    // Remove path class and reset background color for path cells
    document.querySelectorAll('.path').forEach(cell => {
        cell.classList.remove('path');
        cell.style.backgroundColor = '#e2f1f7';
    });
}

export function renderPath(path) {
    path.forEach(([x, y]) => {
        if ((x === startCell.row && y === startCell.col) || (x === endCell.row && y === endCell.col)) {
            return; // Do not apply path color to start and end cells
        }
        const cell = document.querySelector(`[data-row="${x}"][data-col="${y}"]`);
        if (cell) {
            cell.classList.add('path');
        }
    })

}

export function animateVisitedCells(visited_cells) {
    return new Promise(resolve => {
        let delay = 0;
        visited_cells.forEach(([x, y], index) => {
            if ((x === startCell.row && y === startCell.col) || (x === endCell.row && y === endCell.col)) {
                return; // Do not apply path color to start and end cells
            }
            const cell = document.querySelector(`[data-row="${x}"][data-col="${y}"]`);
            if (cell) {
                setTimeout(() => {
                    cell.classList.add('visited');
                    // Apply the gradient background color for visited cells
                    cell.style.transition = 'background-color 0.1s'; // Smooth transition for color change
                    cell.style.backgroundColor = getGradientColor(index, visited_cells.length);
                }, delay);
            }
            delay += window.mazeSpeed; // Increase delay for each step to animate
        });

        // Resolve the promise after all visited cells are animated
        setTimeout(resolve, delay);
    });
}

function getGradientColor(index, total) {
    const ratio = index / total;

    // Starting color: #95e5dd 
    const startR = 149;
    const startG = 229;
    const startB = 221;

    // Ending color: #48c2ec
    const endR = 72;
    const endG = 194;
    const endB = 236;

    // Interpolate between start and end colors
    const r = Math.floor(startR + (endR - startR) * ratio);
    const g = Math.floor(startG + (endG - startG) * ratio);
    const b = Math.floor(startB + (endB - startB) * ratio);

    return `rgb(${r}, ${g}, ${b})`;
}