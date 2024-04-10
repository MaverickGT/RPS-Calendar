const handleUpdate = () => {
    location.href = "http://localhost:8081/api/admin/update"
}

const handleFetchEvents = () => {
    return fetch('/api/items')
        .then(response => response.json())
        .catch(error => console.error('Error fetching data:', error));
}

const handleFetchEvent = (id) => {
    return fetch(`/api/items/${id}`)
        .then(response => response.json())
        .catch(error => console.error('Error fetching data:', error));
}

const handleSelectOption = (option) => {
    console.log(option);
}

const createOption = (event) => {
    const option = document.createElement('option');
    option.value = event.id;
    option.textContent = event.name;

    return option;
}

const handleRenderSelectedEvent = async (eventId) => {
    const events = await handleFetchEvents();
    const event = events.find(({ id }) => id === eventId);
    
    const { location, description, start_time, end_time, start_date, end_date } = event;
    const eventLocationInput = document.getElementById('event-location');
    const eventDescriptionTextarea = document.getElementById('event-description');
    const startTimeInput = document.getElementById('start-time');
    const endTimeInput = document.getElementById('end-time');
    const startDateInput = document.getElementById('start-date');
    const endDateInput = document.getElementById('end-date');

    eventLocationInput.value = location;
    eventDescriptionTextarea.value = description;
    startTimeInput.value = start_time;
    endTimeInput.value = end_time;
    startDateInput.value = start_date;
    endDateInput.value = end_date;
}

const handleRenderEvents = async () => {
    const events = await handleFetchEvents();
    const eventNameDropdown = document.getElementById('event-name');

    events.forEach(event => {
        const option = createOption(event);
        eventNameDropdown.appendChild(option);
    });

    eventNameDropdown.addEventListener("change", (e) => {
        handleRenderSelectedEvent(Number(e.target.value));
    })
}

handleRenderEvents();
