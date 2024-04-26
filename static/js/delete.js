const handleDelete = () => {
  location.href = `${BASE_URL}/api/admin/delete`;
};

const handleUpdate = () => {
  location.href = `${BASE_URL}/api/admin/update`;
};

const handleCreate = () => {
  location.href = `${BASE_URL}/api/admin/create`;
};

const handleFeedback = () => {
  location.href = `${BASE_URL}/api/admin/feedback`;
};

const handleCalendar = () => {
  localStorage.removeItem("hpe-jtw");
  location.href = `${BASE_URL}/`;
};

const handleFetchEvents = () => {
  return fetch("/api/items")
    .then((response) => response.json())
    .catch((error) => console.error("Error fetching data:", error));
};

const createOption = (event) => {
  const option = document.createElement("option");
  option.value = event.id;
  option.textContent = event.name;

  return option;
};

const handleRenderEvents = async () => {
  const events = await handleFetchEvents();
  const eventNameDropdown = document.getElementById("event-name");
  eventNameDropdown.innerHTML = "";

  events.forEach((event) => {
    const option = createOption(event);
    eventNameDropdown.appendChild(option);
  });
};

const handleDeleteEvent = () => {
  const select = document.getElementById("event-name");
  const eventId = Number(select.value);
  const token = localStorage.getItem("hpe-jtw");

  fetch(`/api/admin/delete/${eventId}`, {
    method: "DELETE",
    headers: {
      Authorization: `Bearer ${token}`,
    },
  })
    .then((response) => {
      if (response.ok) {
        handleRenderEvents();
        console.log("Event deleted successfully");
      } else {
        console.error("Failed to delete event");
      }
    })
    .catch((error) => console.error("Error deleting event:", error));
};

handleRenderEvents();
