window.onload = function( ){
  let d = new Date( );
  document.querySelector("#date-picker").value = `${d.getFullYear()}-${d.getMonth()}-${d.getDate()}`;
  document.querySelector("#add-btn").onclick = addNewColumns;
  document.querySelector("#date-picker").onchange = loadColumns;
  document.querySelector("#close-new-columns").onclick = closeNewColumns;
  // document.querySelector("#new-columns").onclick = closeNewColumns;
  loadColumns( );
}

function loadColumns( ){
}

function addNewColumns( ){
  let d = new Date();
  document.querySelector("#timing").value = `${d.getHours()}:${d.getMinutes()}`;
  document.querySelector("#new-columns").classList.remove("new-columns-hide");
  document.querySelector("#new-columns").classList.add("new-columns-show");
}

function closeNewColumns( ){
  document.querySelector("#new-columns").classList.add("new-columns-hide");
  document.querySelector("#new-columns").classList.remove("new-columns-show");

}