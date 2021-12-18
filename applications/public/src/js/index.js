window.onload = function( ){
  let d = new Date( );
  document.querySelector("#date-picker").value = `${d.getFullYear()}-${zeroStuffing(2, d.getMonth())}-${zeroStuffing(2, d.getDate())}`;
  document.querySelector("#add-btn").onclick = addNewColumns;
  document.querySelector("#date-picker").onchange = loadColumns;
  document.querySelector("#close-new-columns").onclick = closeNewColumns;
  document.querySelector("#new-option").onchange = showActiveOption;
  // document.querySelector("#new-columns").onclick = closeNewColumns;
  loadColumns( );
}

function loadColumns( ){
}

function zeroStuffing( len, str ){
  return (new Array(len).fill(0).join('') + str).substr(-len);
}

function addNewColumns( ){
  let d = new Date();
  document.querySelector("#timing").value = `${zeroStuffing(2, d.getHours())}:${zeroStuffing(2, d.getMinutes())}`;
  document.querySelector("#new-columns").classList.remove("new-columns-hide");
  document.querySelector("#new-columns").classList.add("new-columns-show");
}

function closeNewColumns( ){
  document.querySelector("#new-columns").classList.add("new-columns-hide");
  document.querySelector("#new-columns").classList.remove("new-columns-show");

}

function showActiveOption( ){
  let opts = document.querySelectorAll(".ctrl-opts");

  for(let opt of opts){
    opt.classList.add("ctrl-opts-hide");
  }
  let el = document.querySelector(`#fill-${this.value}`);
  if( el ){
    document.querySelector(`#fill-${this.value}`).classList.remove('ctrl-opts-hide');
  }
}