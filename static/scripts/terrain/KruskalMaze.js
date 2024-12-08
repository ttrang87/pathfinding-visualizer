document.getElementById('KruskalMazeButton').addEventListener('click', async () => {
    const animate = document.getElementById('AnimateCheckbox').checked; // Check if animation is enabled

    const data = {
        rows: defaultrows,
        cols: defaultcols,
        start: [startCell.row, startCell.col],
        end: [endCell.row, endCell.col],
        animate: animate  
    };

    try {
        const response = await axios.post('/maze/kruskal', data);
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


function renderMaze(maze, rows, cols) {
    gridContainer.innerHTML = '';

    gridContainer.style.gridTemplateColumns = `repeat(${cols}, ${cellSize}px)`;
    gridContainer.style.gridTemplateRows = `repeat(${rows}, ${cellSize}px)`;

    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            const cell = document.createElement('div');
            cell.classList.add('grid-cell');
            cell.dataset.row = r;
            cell.dataset.col = c;


            if (maze[r][c] === 1) {
                cell.classList.add('maze-cell');
            }

            if (c === startCell.col && r === startCell.row) {
                cell.classList.add('start-cell');
            } else if (c === endCell.col && r === endCell.row) {
                cell.classList.add('end-cell');
            }

            cell.addEventListener('mousedown', () => {
                if (r === startCell.row && c === startCell.col) {
                    isDraggingStart = true;
                } else if (r === endCell.row && c === endCell.col) {
                    isDraggingEnd = true;
                }
            });

            cell.addEventListener('mouseup', () => {
                isDraggingStart = false;
                isDraggingEnd = false;
            });

            cell.addEventListener('mousemove', () => {
                if (isDraggingStart) {
                    update(startCell, r, c, 'start-cell');
                } else if (isDraggingEnd) {
                    update(endCell, r, c, 'end-cell');
                }
            });

            gridContainer.appendChild(cell);
        }
    }
}

function animateMaze(steps, rows, cols) {
    gridContainer.innerHTML = '';
    gridContainer.style.gridTemplateColumns = `repeat(${cols}, ${cellSize}px)`;
    gridContainer.style.gridTemplateRows = `repeat(${rows}, ${cellSize}px)`;

    const cells = [];
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            const cell = document.createElement('div');
            cell.classList.add('grid-cell');
            cell.dataset.row = r;
            cell.dataset.col = c;

            cell.addEventListener('mousedown', () => {
                if (r === startCell.row && c === startCell.col) {
                    isDraggingStart = true;
                } else if (r === endCell.row && c === endCell.col) {
                    isDraggingEnd = true;
                }
            });

            cell.addEventListener('mouseup', () => {
                isDraggingStart = false;
                isDraggingEnd = false;
            });

            cell.addEventListener('mousemove', () => {
                if (isDraggingStart) {
                    update(startCell, r, c, 'start-cell');
                } else if (isDraggingEnd) {
                    update(endCell, r, c, 'end-cell');
                }
            });

            gridContainer.appendChild(cell);
            cells.push(cell);
        }
    }

    let currentStep = 0;

    function drawStep() {
        const maze = steps[currentStep];
        cells.forEach((cell) => {
            const r = parseInt(cell.dataset.row);
            const c = parseInt(cell.dataset.col);

            cell.className = 'grid-cell'; // Reset class
            if (maze[r][c] === 1) {
                cell.classList.add('maze-cell');
            }

            if (r === startCell.row && c === startCell.col) {
                cell.classList.add('start-cell');
            } else if (r === endCell.row && c === endCell.col) {
                cell.classList.add('end-cell');
            }
        });

        currentStep++;
        if (currentStep < steps.length) {
            setTimeout(drawStep, 40); 
        }
    }

    drawStep();
}

function update(cell, newRow, newCol, type) {
    const oldCell = document.querySelector(`[data-row='${cell.row}'][data-col='${cell.col}']`);
    oldCell.classList.remove(type);

    cell.row = newRow;
    cell.col = newCol;

    const newCell = document.querySelector(`[data-row='${newRow}'][data-col='${newCol}']`);
    newCell.classList.add(type);
}
