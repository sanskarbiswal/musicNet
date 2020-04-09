// Local JS Function
function playFromURL(){
    // Get URL from User
    url = document.getElementById('t_URL').value;
    console.log(url);
    eel.generate_url(url);
    //eel.test();
}
function appStart(){
    eel.on_SysStart();
}
// EEL Exposed Functions
eel.expose(music_url);
function music_url(url, metaData){
    // Update Meta Data
    document.getElementById('thumb_img').src=metaData.thumb;
    document.getElementById('music_name').innerHTML=metaData.title;
    // Start Music
    document.getElementById('audSrc').setAttribute('src', url);
}

eel.expose(create_user_modal);
function create_user_modal(){
    
}

window.onload=appStart;
