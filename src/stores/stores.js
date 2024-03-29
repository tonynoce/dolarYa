import {writable, readable} from "svelte/store"


export let USDprice = writable()
export let ARSprice = writable()

const urlUSD = "https://api.yadio.io/exrates/USD"
const urlARS = "https://api.yadio.io/exrates/ARS"

export let dataARS;
export let dataUSD;


/**
 * @dev this function gets the rate
 * it also writes is to the local storage
 */
export const getRate = async() => {
  let responseUSD = await fetch(urlUSD);
  dataUSD = await responseUSD.json();

  dataUSD = {ARStoUSD : dataUSD.USD.ARS};
  dataUSD = dataUSD.ARStoUSD;
  
  let responseARS = await fetch(urlARS);
  dataARS = await responseARS.json();
  
  dataARS = {USDtoARS : dataARS.ARS.USD};
  dataARS = dataARS.USDtoARS;

  // USDprice.set(dataUSD.toFixed(2));
  USDprice.set(dataUSD);
  ARSprice.set(dataARS);
  //return Number(dataUSD).toFixed(2);

  // write to local storage:
/*   localStorage.setItem('USDprice', dataARS);
  localStorage.setItem('ARSprice', dataUSD);
  localStorage.setItem('Date', String(Date.now())); */
} 
