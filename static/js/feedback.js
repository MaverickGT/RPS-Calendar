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

const handleDeleteAllFeedback = () => {
    fetch(`/api/feedback`, { method: 'DELETE' }).then(() => window.location.reload());
}

const handleFetchFeedbacks = async () => {
    return fetch("/api/feedback").then((res) => res.json());
};

const handleDeleteFeedbackById = (feedbackId) => {
    fetch(`/api/feedback/${feedbackId}`, { method: 'DELETE' }).then(() => window.location.reload());
};

const handleCreateFeedbackElement = (feedback) => {
    const { id, name, email, description: comment } = feedback;

    const feedbackElement = document.createElement("div");
    const feedbackElementContent = document.createElement("div")
    const feedbackElementAuthor = document.createElement("label")
    const feedbackElementComment = document.createElement("p")
    const feedbackElementDeleteButton = document.createElement("button")

    feedbackElement.setAttribute("class", "feedback-item");
    feedbackElementContent.setAttribute("class", "feedback-item-content");
    feedbackElementAuthor.setAttribute("class", "feedback-item-author");
    feedbackElementComment.setAttribute("class", "feedback-item-comment");
    feedbackElementDeleteButton.setAttribute("class", "feedback-item-delete-btn");

    feedbackElementDeleteButton.addEventListener("click", () => handleDeleteFeedbackById(id))

    feedbackElementAuthor.innerText = `${name}, ${email}`;
    feedbackElementComment.innerText = comment;
    feedbackElementDeleteButton.innerText = 'Delete';

    feedbackElement.appendChild(feedbackElementContent);
    feedbackElement.appendChild(feedbackElementDeleteButton);
    feedbackElementContent.appendChild(feedbackElementAuthor);
    feedbackElementContent.appendChild(feedbackElementComment);

    return feedbackElement;
}

const handleRenderNoFeedbacksMessage = () => {
    const noFeedbackMessage = document.createElement("p")
    noFeedbackMessage.setAttribute("class", "no-feedback-msg")
    noFeedbackMessage.innerText = "No feedback available."

    return noFeedbackMessage;
};

const renderFeedbacks = async () => {
    const feedbacks = await handleFetchFeedbacks();
    const feedbackContainer = document.getElementById("feedbacks-container");

    if (feedbacks.length === 0) {
        const feedbackElement = handleRenderNoFeedbacksMessage();
        feedbackContainer.appendChild(feedbackElement)
    }

    feedbacks.forEach((feedback) => {
        const feedbackElement = handleCreateFeedbackElement(feedback);
        feedbackContainer.appendChild(feedbackElement);
    });
}

renderFeedbacks();

