


async function get() {
    let response = await fetch('http://localhost:8000/api/court-types/', {
        method: "GET",
        headers: {
            "Accept": "application/json"
        }
    });
    data = await response.json();
    let d = document.getElementById('list');
    data.forEach(court => {
       const li = document.createElement('li');
       li.innerHTML = court.name;
       d.appendChild(li);
        
    });
}

get();