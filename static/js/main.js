function getValue() {
  var name = document.getElementById("name").value;
  var email = document.getElementById("email").value;
  var message = document.getElementById("feedback_text").value;

  var data = {
    name: name,
    email: email,
    feedback: message,
  };
  return data;
}
function clearFeedback() {
  document.getElementById("name").value = "";
  document.getElementById("email").value = "";
  document.getElementById("feedback_text").value = "";
}

function submitFeedback() {
  var data = getValue();
  console.log(data);
  fetch("http://localhost:8081/api/feedback", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      clearFeedback();
    });
}

function getEvents() {
  fetch("http://localhost:8081/api/items")
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      var events = data.data;
      var eventList = document.getElementById("eventList");
      eventList.innerHTML = "";
      events.forEach((event) => {
        var eventItem = document.createElement("li");
        eventItem.innerHTML = event.name;
        eventList.appendChild(eventItem);
      });
    });
}

function loadCalendar() {
  document.addEventListener("DOMContentLoaded", function () {
    var calendarEl = document.getElementById("calendar");
    var calendar = new FullCalendar.Calendar(calendarEl, {
      initialView: "dayGridMonth",
    });
    calendar.render();
    calendar.updateSize();
  });
}
