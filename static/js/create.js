const handleDelete = () => {
    location.href = "http://localhost:8081/api/admin/delete"
}

const handleUpdate = () => {
    location.href = "http://localhost:8081/api/admin/update"
}

const handleCreate = () => {
    location.href = "http://localhost:8081/api/admin/create"
}

const handleCalendar = () => {
    localStorage.removeItem("hpe-jtw")
    location.href = "http://localhost:8081/"
}

const handleSubmitEvent = () => {
    const eventLocation = document.getElementById('event-location').value;
    const eventDescription = document.getElementById('event-description').value;
    const startTime = document.getElementById('start-time').value;
    const endTime = document.getElementById('end-time').value;
    const startDate = document.getElementById('start-date').value;
    const endDate = document.getElementById('end-date').value;
    const eventName = document.getElementById('event-name').value;
    const eventType = document.getElementById('event-type').value;
    const jwtToken = localStorage.getItem("hpe-jtw");
    const body = {
        name: eventName,
        start_date: startDate,
        end_date: endDate,
        type: eventType,
        color: "",
        description: eventDescription,
        picture: "",
        start_time: startTime,
        end_time: endTime,
        all_day: false,
        location: eventLocation,
    };

    fetch("http://localhost:8081/api/admin/add", { method: "POST", body: JSON.stringify(body), headers: { "Authorization": `Bearer ${jwtToken}`, 'Content-Type': "application/json" } }).then((res) => console.log(res));
}
