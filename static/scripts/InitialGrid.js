const gridContainer = document.getElementById("grid");
const cellSize = 40;

const defaultcols = 31;
const defaultrows = 13;

let startCell = { row: 3, col: 4 }; 
let endCell = { row: 10, col: 27 }; 

let isDraggingStart = false;
let isDraggingEnd = false;


function createGrid() {
    gridContainer.innerHTML = "";

    const containerWidth = window.innerWidth;
    const containerHeight = window.innerHeight - 80;

    const cols = Math.floor(containerWidth / cellSize);
    const rows = Math.floor(containerHeight / cellSize);

    gridContainer.style.gridTemplateColumns = `repeat(${cols}, ${cellSize}px)`;
    gridContainer.style.gridTemplateRows = `repeat(${rows}, ${cellSize}px)`;

    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            const cell = document.createElement("div");
            cell.classList.add("grid-cell");
            cell.dataset.row = row;
            cell.dataset.col = col;
            cell.addEventListener("click", () => {
                const x = cell.dataset.row;
                const y = cell.dataset.col;
                console.log(`Cell clicked: (${x}, ${y})`);
            });

            if (row === startCell.row && col === startCell.col) {
                cell.classList.add("start-cell");
            } else if (row === endCell.row && col === endCell.col) {
                cell.classList.add("end-cell");
            }

            cell.addEventListener("mousedown", () => {
                if (row === startCell.row && col === startCell.col) {
                    isDraggingStart = true;
                } else if (row === endCell.row && col === endCell.col) {
                    isDraggingEnd = true;
                }
            });

            cell.addEventListener("mouseup", () => {
                isDraggingStart = false;
                isDraggingEnd = false;
            });

            cell.addEventListener("mousemove", () => {
                if (isDraggingStart) {
                    startCell = { row, col };
                    console.log(`Start Cell moved to: (${startCell.row}, ${startCell.col})`);
                    createGrid(); // Redraw grid to reflect new position
                } else if (isDraggingEnd) {
                    endCell = { row, col };
                    console.log(`End Cell moved to: (${endCell.row}, ${endCell.col})`);
                    createGrid();
                }
            });

            gridContainer.appendChild(cell);
        }
    }
}

createGrid();

