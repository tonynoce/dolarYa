<script lang="ts">
    import {fly} from "svelte/transition"

    export let showMe = false;

    export function hide() {
        showMe = false
    }
</script>

{#if (showMe === true)}
    <modal transition:fly="{{ x: -200, duration: 750 }}">
        <div class="wrapper">
            <div class = "modal">
                <!-- SLOT -->
                <slot/>
                <!-- Close button -->
                <div class="buttonWrapper"> 
                    <button
                    on:click={() => showMe = false}
                    >Cerrame</button>
                </div>
            </div>
        </div>
    </modal>
{/if}


<style>
    .wrapper{
        background-color: rgba(14, 31, 43, 0.75);
        position: fixed;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
    }
    
    .modal {
        border-radius: 5px;
        max-width: 500px;
        padding: 5%;
        margin: 15% auto;
        background-image: radial-gradient(farthest-corner at 20px 20px,rgba(31, 127, 172, 0.7) 25%, rgba(135, 20, 189, 0.25) 80%);
        background-color: rgb(10, 48, 73, 1);
    }

    .buttonWrapper {
        margin-top: 10%;
        text-align: right;
    }

</style>