import {writable, readable} from "svelte/store"


export let USDprice = writable()
export let ARSprice = writable()

let url = "https://api.yadio.io/exrates/USD"


export const getRate = async() => {
    let response = await fetch(url);
    let data = await response.json();
    data = await {ARStoUSD : data.USD.ARS};
    data = data.ARStoUSD;
    USDprice.set(data.toFixed(2));
    return Number(data).toFixed(2);
  } 
