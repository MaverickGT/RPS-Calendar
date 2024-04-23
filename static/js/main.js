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
  fetch("http://127.0.0.1:8081/api/feedback", {
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

async function getEvents() {
  var return_data = [];
  await fetch("http://127.0.0.1:8081/api/items")
    .then((res) => res.json())
    .then((data) => {
      return_data = data;
    });
  return return_data;
}

async function loadCalendar() {
  var events_data = await getEvents();
  var events = [];
  for (var i = 0; i < events_data.length; i++) {
    var event = {
      title: events_data[i].name,
      start: events_data[i].start_date,
      end: events_data[i].end_date,
      color: events_data[i].color,
      textColor: "black",
      extendedProps: {
        description: events_data[i].description,
        location: events_data[i].location,
        image: events_data[i].picture,
        start_time: events_data[i].start_time,
        end_time: events_data[i].end_time,
      },
    };
    events.push(event);
  }
  console.log(events);

  var calendarEl = document.getElementById("calendar");
  var calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: "dayGridMonth",
    events: events,
    eventClick: function (info) {
      var event = info.event;
      var start_time = event.extendedProps.start_time;
      var end_time = event.extendedProps.end_time;
      var title = event.title;
      var description = event.extendedProps.description;
      var location = event.extendedProps.location;
      var image = event.extendedProps.image;
      console.log(event);
      document.getElementById("modal-title").innerHTML = title;
      document.getElementById("modal-description").innerHTML = description;
      document
        .getElementById("modal-location-link")
        .setAttribute("href", location);
      document.getElementById("modal-start-time").innerHTML = start_time;
      document.getElementById("modal-end-time").innerHTML = end_time;
      document
        .getElementById("modal-image")
        .setAttribute("src", "/static/images/" + image);
      document.getElementById("modal").classList.add("active");
      document.getElementById("overlay").classList.add("active");
      const closeModalButton = document.querySelectorAll("[data-close-button]");
      closeModalButton.forEach((button) => {
        button.addEventListener("click", () => {
          const modal = button.closest(".modal");
          closeModal(modal);
        });
      });
    },
  });
  calendar.render();
  calendar.updateSize();
}

function closeModal(modal) {
  if (modal == null) return;
  modal.classList.remove("active");
  overlay.classList.remove("active");
}

var myVar;
window.onload = function () {
  loadCalendar()
    .then(() => {
      console.log("Calendar loaded");
    })
    .catch((error) => {
      console.error("Error loading calendar:", error);
    });
  myVar = setTimeout(showPage, 300);
};

function showPage() {
  document.getElementById("loader").style.display = "none";
  document.getElementById("loader-background").style.display = "none";
}
