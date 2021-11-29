let video = document.querySelector("#video");

document.querySelector("#inicio").addEventListener("click", function(ev){
    navigator.mediaDevices.getUserMedia({audio: false, video:true})
    .then(record)
    .catch(err => console.log(err));
})

let chunks = [];

function record(stream){
    video.srcObject = stream;

    //grabar
    let mediaRecorder = new MediaRecorder(stream, {
        mimeType: 'video/mp4;codecs=h264'
    });


    //comenzar a grabar
    mediaRecorder.start()

    mediaRecorder.ondataavailable = function(e){
        chunks.push(e.data);
        console.log(e.data);
    }

    mediaRecorder.onstop = function(){
        alert("Grabacion finalizada...")

        //crear archivo largo para almacenar video
        let blob = new Blob(chunks, {type: "video/mp4"});
        chunks = [];

        download(blob);

    }
    

    document.querySelector("#inicio").addEventListener("click", function(ev){
        mediaRecorder.stop();
        alert("detenido");
    })

    

}


function download(blob){
    let link = document.createElement("input");
    link.name = "respuesta_video";
    link.id = "id_respuesta_video";
    link.setAttribute("value",blob);
    link.setAttribute("src",blob);
    link.style.display = 'none';

    document.body.appendChild(link);    
}