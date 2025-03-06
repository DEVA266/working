/* function rock(){
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
} */
  let score = JSON.parse(localStorage.getItem("score")) || {
    Wins:0,
    Loss:0,
    Tie:0
  };
     

  /* the most useful function called default operator || 
  int his operator it consist of two operands ex a || b
  if a is true then a will be excueted, if a is false b will get exceuted
  in the above function while clickig the rest button the 
  json propety will goes to null because we remove the local storage
  in that time while json property get false, 
  the b option i mean the default value for will be exceuted */
  
  
  /*if (score === null) {
    score:Wins=0,
    score:Loss=0,
    score:Tie=0
  };*/

  
    function gameplay(playermove) {
    const computermove = computeroption();
    let result = " ";
    

    if (playermove === "scissor") {
      if(computermove === "rock"){
        result = "You Loss the Game"; 
      }
      else if(computermove === "paper"){
        result = "You Win the Game";
      }
      else {
        result = "the match is Tie";
      }
      }
      
    else if (playermove === "paper"){
        
        if(computermove === "rock"){
          result = "You Win the Game";
          
        }
        else if(computermove === "paper"){
          result = "the match is Tie";
          
        }
        else {
          result = "You Loss the Game";
        }
            }
      
    else if (playermove === "rock"){
        if(computermove === "rock"){
          result = "the match is Tie";
        }
        else if(computermove === "paper"){
          result = "You Loss the Game";
        }
        else {
          result = "You Win the Game";
        }
    }

      if (result === "You Win the Game"){
        score.Wins += 1;
      }
      else if (result === "You Loss the Game"){
        score.Loss += 1;
      }
      else if (result === "the match is Tie") {
        score.Tie += 1;
      }

      localStorage.setItem("score" , JSON.stringify(score));

      document.querySelector('jsresult').innerHTML = result;

      alert(`You picked ${playermove}, computer picked ${computermove} . ${result}
Wins : ${score.Wins}  Loss : ${score.Loss}  Tie : ${score.Tie}`);
  }

  function computeroption(){
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
    return computermove;
  }

  