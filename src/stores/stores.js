import {writable, readable} from "svelte/store"


export let USDprice = writable()
export let ARSprice = writable()

const urlUSD = "https://api.yadio.io/exrates/USD"
const urlARS = "https://api.yadio.io/exrates/ARS"

/**
 * @dev this function gets the rate of just the usd
 */
export const getRate = async() => {
  let responseUSD = await fetch(urlUSD);
  let dataUSD = await responseUSD.json();
  
  let responseARS = await fetch(urlARS);
  let dataARS = await responseARS.json();

  dataUSD = {ARStoUSD : dataUSD.USD.ARS};
  dataUSD = dataUSD.ARStoUSD;
  
  dataARS = {USDtoARS : dataARS.ARS.USD};
  dataARS = dataARS.USDtoARS;

  // USDprice.set(dataUSD.toFixed(2));
  USDprice.set(dataUSD);
  ARSprice.set(dataARS);
  //return Number(dataUSD).toFixed(2);
} 
