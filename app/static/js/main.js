function toggleFav(elem){

    const favBtnHtml = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-bookmark-check-fill" viewBox="0 0 16 16"> \
        <path fill-rule="evenodd" d="M2 15.5V2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.74.439L8 13.069l-5.26 2.87A.5.5 0 0 1 2 15.5zm8.854-9.646a.5.5 0 0 0-.708-.708L7.5 7.793 6.354 6.646a.5.5 0 1 0-.708.708l1.5 1.5a.5.5 0 0 0 .708 0l3-3z"/>\
        </svg>';
    const notFavBtnHtml = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-bookmark-plus" viewBox="0 0 16 16"> \
        <path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5V2zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1H4z"/> \
        <path d="M8 4a.5.5 0 0 1 .5.5V6H10a.5.5 0 0 1 0 1H8.5v1.5a.5.5 0 0 1-1 0V7H6a.5.5 0 0 1 0-1h1.5V4.5A.5.5 0 0 1 8 4z"/> \
        </svg>';
    var fav = 1;
        
    if (elem.classList.contains("fav-0")){
        elem.classList.replace("fav-0", "fav-1");
        elem.innerHTML = favBtnHtml;
    } else {
        fav = 0;
        elem.classList.replace("fav-1", "fav-0");
        elem.innerHTML = notFavBtnHtml;
    }

    const request = new XMLHttpRequest();
    request.open('POST', '/toggle_fav');

    request.onload = () => {

        const data = JSON.parse(request.responseText);

        if (data.success) {
            console.log('Success!');

        }
        else {
            console.log('There was an error.');
        }
    }

    const data = new FormData();
    data.append('id', elem["id"]);
    data.append('fav', fav);

    request.send(data);
    return false;
};

window.onload = function() {

    console.log('Script loaded!')
    
};