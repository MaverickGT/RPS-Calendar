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
    const event = await handleFetchEvent(eventId);
    console.log(event);
}

const handleRenderEvents = async () => {
    const events = await handleFetchEvents();
    const eventNameDropdown = document.getElementById('event-name');

    events.forEach(event => {
        const option = createOption(event);
        eventNameDropdown.appendChild(option);
    });

    eventNameDropdown.addEventListener("change", (e) => {
        handleRenderSelectedEvent(e.target.value);
    })
}


handleRenderEvents();
