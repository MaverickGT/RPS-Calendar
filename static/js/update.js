const handleDelete = () => {
  location.href = "http://eventia.eu.hpecorp.net/api/admin/delete";
};

const handleUpdate = () => {
  location.href = "http://eventia.eu.hpecorp.net/api/admin/update";
};

const handleCreate = () => {
  location.href = "http://eventia.eu.hpecorp.net/api/admin/create";
};

const handleCalendar = () => {
  localStorage.removeItem("hpe-jtw");
  location.href = "http://eventia.eu.hpecorp.net/";
};

const handleFetchEvents = () => {
  return fetch("/api/items")
    .then((response) => response.json())
    .catch((error) => console.error("Error fetching data:", error));
};

const handleFetchEvent = (id) => {
  return fetch(`/api/items/${id}`)
    .then((response) => response.json())
    .catch((error) => console.error("Error fetching data:", error));
};

const handleSelectOption = (option) => {
  console.log(option);
};

const createOption = (event) => {
  const option = document.createElement("option");
  option.value = event.id;
  option.textContent = event.name;

  return option;
};

const handleRenderSelectedEvent = async (eventId) => {
  const events = await handleFetchEvents();
  const event = events.find(({ id }) => id === eventId);

  const { location, description, start_time, end_time, start_date, end_date } =
    event;
  const eventLocationInput = document.getElementById("event-location");
  const eventDescriptionTextarea = document.getElementById("event-description");
  const startTimeInput = document.getElementById("start-time");
  const endTimeInput = document.getElementById("end-time");
  const startDateInput = document.getElementById("start-date");
  const endDateInput = document.getElementById("end-date");

  eventLocationInput.value = location;
  eventDescriptionTextarea.value = description;
  startTimeInput.value = start_time;
  endTimeInput.value = end_time;
  startDateInput.value = start_date;
  endDateInput.value = end_date;
};

const handleRenderEvents = async () => {
  const events = await handleFetchEvents();
  const eventNameDropdown = document.getElementById("event-name");

  events.forEach((event) => {
    const option = createOption(event);
    eventNameDropdown.appendChild(option);
  });

  eventNameDropdown.addEventListener("change", (e) => {
    handleRenderSelectedEvent(Number(e.target.value));
  });
};

handleRenderEvents();

const handleUpdateEvent = () => {
  const eventLocation = document.getElementById("event-location").value;
  const eventDescription = document.getElementById("event-description").value;
  const startTime = document.getElementById("start-time").value;
  const endTime = document.getElementById("end-time").value;
  const startDate = document.getElementById("start-date").value;
  const endDate = document.getElementById("end-date").value;
  const eventName = document.getElementById("event-name").textContent;
  const eventType = document.getElementById("event-type").value;
  const jwtToken = localStorage.getItem("hpe-jtw");

  const selectedEvent = document.getElementById("event-name");
  const eventId = Number(selectedEvent.value);

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

  fetch(`/api/admin/update/${eventId}`, {
    method: "PUT",
    body: JSON.stringify(body),
    headers: {
      Authorization: `Bearer ${jwtToken}`,
      "Content-Type": "application/json",
    },
  }).then((res) => console.log(res));
};
