// function uploadFiles() {
//   var files = document.getElementById('file_upload').files;
//   if(files.length==0){
//       alert("Please first choose or drop any file(s)...");
//       return;
//   }
//   var filenames="";
//   for(var i=0;i<files.length;i++){
//       filenames+=files[i].name+"\n";
//   }
//   alert("Selected file(s) :\n________\n"+filenames);
// }
// function deleteFiles(){
// document.getElementById("files-form").reset();
// } 

async function uploadFile() {

  const file = document.getElementById("file_upload").files[0];
  let fileId = Math.random().toString(36).slice(2, 8);


  let formData = new FormData();
  formData.append("file", file, `${fileId}.jpg`);
  await fetch('/upload', {
    method: "POST", 
    body: formData
  }); 
  alert('The file has been uploaded successfully.');
}

 