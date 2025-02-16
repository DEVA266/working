function rock(){
  const randomnumber = Math.random();
  console.log(randomnumber);
  let computermove = " ";
  if ( randomnumber >=0 && randomnumber < 1/3){
    computermove = "rock";
  }
  else if (randomnumber >=1/3 && randomnumber < 2/3 ){
    computermove = "paper";
  }
  else {
    computermove = "scissor";
  }
  console.log(computermove);

  let result = " ";
  if(computermove === "rock"){
    result = "the match is Tie";
  }
  else if(computermove === "paper"){
    result = "You Loss the Game";
  }
  else {
    result = "You Win the Game";
  }
  alert(`You picked Rock, computer picked ${computermove} . ${result}`);
}

function paper(){
  const randomnumber = Math.random();
  console.log(randomnumber);
  let computermove = " ";
  if ( randomnumber >=0 && randomnumber < 1/3){
    computermove = "paper";
  }
  else if (randomnumber >=1/3 && randomnumber < 2/3 ){
    computermove = "scissor";
  }
  else {
    computermove = "rock";
  }
  console.log(computermove);

  let result = " ";
  if(computermove === "rock"){
    result = "You Win the Game";
    
  }
  else if(computermove === "paper"){
    result = "the match is Tie";
    
  }
  else {
    result = "You Loss the Game";
  }
  alert(`You picked Paper, computer picked ${computermove} . ${result}`);
}

function scissor(){
  const randomnumber = Math.random();
  console.log(randomnumber);
  let computermove = " ";
  if ( randomnumber >=0 && randomnumber < 1/3){
    computermove = "scissor";
  }
  else if (randomnumber >=1/3 && randomnumber < 2/3 ){
    computermove = "rock";
  }
  else {
    computermove = "paper";
  }
  console.log(computermove);

  let result = " ";
  if(computermove === "rock"){
    result = "You Loss the Game";
    
    
  }
  else if(computermove === "paper"){
    result = "You Win the Game";
  }
  else {
    result = "the match is Tie";
  }
  alert(`You picked Scissor, computer picked ${computermove} . ${result}`);
}