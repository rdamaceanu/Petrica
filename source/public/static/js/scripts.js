/* static/js/scripts.js */

// Function to load day parts from the backend
async function loadDayParts() {
    try {
        const response = await fetch('/api/dayparts'); // Endpoint to fetch day parts
        const dayParts = await response.json();

        const container = document.getElementById('dayparts-container');
        container.innerHTML = ''; // Clear existing content

        dayParts.forEach(dayPart => {
            const dayPartDiv = document.createElement('div');
            dayPartDiv.className = 'daypart';

            const dayPartTitle = document.createElement('h3');
            dayPartTitle.textContent = dayPart.name;
            dayPartDiv.appendChild(dayPartTitle);

            if (dayPart.minitasks && dayPart.minitasks.length > 0) {
                const minitaskList = document.createElement('ul');
                minitaskList.className = 'minitask';

                dayPart.minitasks.forEach(task => {
                    const taskItem = document.createElement('li');
                    taskItem.textContent = task.description;
                    minitaskList.appendChild(taskItem);
                });

                dayPartDiv.appendChild(minitaskList);
            }

            container.appendChild(dayPartDiv);
        });
    } catch (error) {
        console.error('Error loading day parts:', error);
    }
}

// Function to save journal content
async function saveJournal() {
    const content = document.getElementById('journal-editor').value;

    try {
        const response = await fetch('/api/journal', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ content })
        });

        if (response.ok) {
            alert('Journal saved successfully!');
        } else {
            alert('Failed to save journal.');
        }
    } catch (error) {
        console.error('Error saving journal:', error);
    }
}

// Event listeners
document.getElementById('save-journal').addEventListener('click', saveJournal);

// Load day parts on page load
window.addEventListener('DOMContentLoaded', loadDayParts);
