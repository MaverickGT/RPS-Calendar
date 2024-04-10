
const handleSubmit = () => {
    const username = document.getElementById("username").value
    const password = document.getElementById("password").value

    fetch("http://localhost:8081/api/admin/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ username, password }),
    })
        .then((res) => res.json())
        .then((data) => {
            if (data.message === 'Bad credentials') {
                alert('Failed to login: ' + data.message);
            } else {
                localStorage.setItem("hpe-jtw", data.access_token)
                location.href="http://localhost:8081/api/admin"
            }
        })
}