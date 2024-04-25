async function addEvent(body) {
  await fetch("localhost:8081/api/admin/add", {
    method: "POST",
    body: JSON.stringify(body),
    headers: {
      Authorization: `Bearer ${jwtToken}`,
      "Content-Type": "application/json",
    },
  }).then((res) => console.log(res));
}

async function uploadImage(file) {
  if (file) {
    const formData = new FormData();
    formData.append("file", file);
    await fetch("localhost:8081/api/upload", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.text())
      .then((text) => {
        console.log("Success:", text);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  } else {
    console.log("No image has been uploaded!");
  }
}

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

const handleSubmitEvent = async () => {
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
  const eventImage = document.getElementById("image-upload");
  const file = eventImage.files[0];
  console.log(file.name);
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
    picture: file.name,
  };
  console.log(body);
  await addEvent(body);
  console.log("after ADD event");
  await uploadImage(file);
  console.log("after upload image");
};
