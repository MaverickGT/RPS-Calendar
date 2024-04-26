const handleDelete = () => {
  location.href = `${BASE_URL}/api/admin/delete`;
};

const handleUpdate = () => {
  location.href = `${BASE_URL}/api/admin/update`;
};

const handleCreate = () => {
  location.href = `${BASE_URL}/api/admin/create`;
};

const handleCalendar = () => {
  localStorage.removeItem("hpe-jtw");
  location.href = `${BASE_URL}/`;
};

const handleSubmitEvent = () => {
  const eventLocation = document.getElementById("event-location").value;
  console.log(eventLocation);
  const eventDescription = document.getElementById("event-description").value;
  console.log(eventDescription);
  const startTime = document.getElementById("start-time").value;
  console.log(startTime);
  const endTime = document.getElementById("end-time").value;
  console.log(endTime);
  const startDate = document.getElementById("start-date").value;
  console.log(startDate);
  const endDate = document.getElementById("end-date").value;
  console.log(endDate);
  const eventName = document.getElementById("event-name").value;
  console.log(eventName);
  const eventType = document.getElementById("event-type").value;
  console.log(eventType);
  const jwtToken = localStorage.getItem("hpe-jtw");
  //const eventImage = document.getElementById("image-upload");

  const body = {
    name: eventName,
    start_date: startDate,
    end_date: endDate,
    type: eventType,
    color: "",
    description: eventDescription,
    start_time: startTime,
    end_time: endTime,
    all_day: false,
    location: eventLocation,
    picture: "",
  };
  console.log(body.picture);
  fetch("http://localhost:8081/api/admin/add", {
    method: "PUT",
    body: JSON.stringify(body),
    headers: {
      Authorization: `Bearer ${jwtToken}`,
      "Content-Type": "application/json",
    },
  }).then((res) => console.log(res));
  clearForm();
  console.log("after ADD event");
};

function clearForm() {
  document.getElementById("event-location").value = "";
  document.getElementById("event-description").value = "";
  document.getElementById("start-time").value = "";
  document.getElementById("end-time").value = "";
  document.getElementById("start-date").value = "";
  document.getElementById("end-date").value = "";
  document.getElementById("event-name").value = "";
}
