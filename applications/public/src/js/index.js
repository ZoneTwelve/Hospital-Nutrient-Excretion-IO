var fillSelectors = {
  'food': [
    {id: 0, name:'營養餐點'}, 
    {id:1, name:'其他'},
  ],
  'poop': [
    {id:0, name:'正常'}, 
    {id:1, name:'異常'}, 
    {id:2, name:'黑色'}, 
    {id:3, name:'咖啡色'}, 
    {id:4, name:'黃色'},
    {id:5,name:'其他'},
  ],
  'pee':  [
      {id:0, name:'乾淨、透明'}, 
      {id:11,name:'便秘'},
      {id:1, name:'淡黃色'}, 
      {id:2, name:'深黃色'}, 
      {id:3, name:'琥珀或蜂蜜色'}, 
      {id:4, name:'橘色'}, 
      {id:6, name:'粉色或紅色'}, 
      {id:7, name:'藍色或綠色'}, 
      {id:8, name:'深褐色'}, 
      {id:9, name:'乳白色'}, 
      {id:10,name:'混濁'},
      {id:11,name:'其他'},
    ],
};

window.onload = function( ){
  let d = new Date( );
  document.querySelector("#date-picker").value = `${d.getFullYear()}-${zeroStuffing(2, d.getMonth())}-${zeroStuffing(2, d.getDate())}`;
  document.querySelector("#add-btn").onclick = addNewColumns;
  // document.querySelector("#date-picker").onchange = loadColumns;
  document.querySelector("#close-new-columns").onclick = closeNewColumns;
  document.querySelector("#new-option").onchange = showActiveOption;
  // document.querySelector("#new-columns").onclick = closeNewColumns;
  for(let form of document.querySelectorAll('[method="COPY"]')){
    console.log( form );
    form.onsubmit = copyFormStatus;
  }
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

function applyFillSelector( label ){
  // result-${label}-selector
  let selector = document.querySelector(`#result-${label}-selector`);

  if( !fillSelectors[ label ] || selector == null )
    return;

  selector.innerHTML = "";

  for(let opt of fillSelectors[ label ]){
    let el = createElement("option", {
      innerText: opt.name,
      value: opt.id
    });
    selector.appendChild( el );
  }
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

  applyFillSelector( this.value );

}

function copyFormStatus( ){
  let data = this.querySelectorAll('[name]');
  let result = [];
  for(let el of data){
    let target = document.querySelector(`#result_form [name="${el.name}"]`);
    target.value = el.value;
    switch(true){
      case /_opt/.test( el.name ):
        let index = el.selectedIndex;
        result.push( el[index].innerText );
      break;
      case /_cap/.test( el.name ):
        if( el.value != "" )
          result.push( `量：${el.value} ${el.unit||""}` );
      break;
      case /_state/.test( el.name ):
        if( el.value!="" )
          result.push( `備註：${el.value}` );
      break;
    }
    // result.push( el.value );
  }
  document.querySelector(`#result-${this.name}`).innerText = result.filter(v=>v.toString()!="").join(',');
  return false;
}

function submitResult( ){
  return false;
}