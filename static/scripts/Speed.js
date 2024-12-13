let timeout = 40; // Default timeout for 'Average'
window.mazeSpeed = timeout; 

function updateSpeed(state) {
    const speed = document.getElementById('speed');
    speed.textContent = state;

    if (state === 'Fast') {
        timeout = 15;
    } else if (state === 'Average') {
        timeout = 40;
    } else if (state === 'Slow') {
        timeout = 180;
    }

    window.mazeSpeed = timeout; // Setting the global variable for timeout
}

document.getElementById('fastBtn').addEventListener('click', function() {
    updateSpeed('Fast');
});

document.getElementById('averageBtn').addEventListener('click', function() {
    updateSpeed('Average');
});

document.getElementById('slowBtn').addEventListener('click', function() {
    updateSpeed('Slow');
});
