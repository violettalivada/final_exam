function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

async function makeRequest(url, method='GET', data=undefined) {
    let opts = {method, headers: {}};
 console.log(method)
    if (!csrfSafeMethod(method))
        opts.headers['X-CSRFToken'] = getCookie('csrftoken');
        console.log(getCookie('csrftoken'))

    if (data) {
        opts.headers['Content-Type'] = 'application/json';
        opts.body = JSON.stringify(data);
    }

    let response = await fetch(url, opts);

    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}

async function addFriend(event) {
    event.preventDefault();
    let addBtn = event.target;
    let url = addBtn.href;
    console.log(addBtn)
    console.log(url);
    try {
        let response = await makeRequest(url, 'POST');
        console.log(response);

    }
    catch (error) {
        console.log(error);
    }

}

async function delFriend(event) {
    event.preventDefault();
    let delBtn = event.target;
    let url = delBtn.href;

    try {
        let response = await makeRequest(url , "DELETE");
        console.log(response);

    }
    catch (error) {
        console.log(error);
    }
}

window.addEventListener('load', function() {
    const addButtons = document.getElementById('add');
    const delButtons = document.getElementById('del');

    for (let btn of addButtons) {btn.onclick = addFriend}
    for (let btn of delButtons) {btn.onclick = delFriend}
});