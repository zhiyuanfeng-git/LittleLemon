function formatTime(time) 
{
    const ampm = time < 12 ? 'AM' : 'PM'
    const t = time < 12 ? time : time > 12 ? time - 12 : time
    const label = `${t} ${ampm}`
    return label
}

function InitNumberGuestsOptions()
{
    slot_options = []
    slot_options += document.getElementById('no_of_guests').innerHTML
    for (var i = 1; i <= 10; i++)
    {
        slot_options += `<option value=${i}>${i}</option>`
    }
    document.getElementById('no_of_guests').innerHTML = slot_options
}

function setElementToday(date)
{
    document.getElementById('today').innerHTML = date
}

function setReservationDate()
{
    const date = new Date()
    const now_date = `${date.getFullYear()}-${(date.getMonth() + 1).toString().padStart(2,"0")}-${date.getDate().toString().padStart(2, '0')}`
    const element_date = document.getElementById('reservation_date')
    element_date.value = now_date
    setElementToday(now_date)
    fetchTheDateBookings(now_date)
    element_date.addEventListener('change',function(e){
        onElementDateChanged(e)
    })
}

function onElementDateChanged(e)
{
    const new_date = document.getElementById('reservation_date').value
    setElementToday(new_date)
    fetchTheDateBookings(new_date)
}

function fetchTheDateBookings(date)
{
    const url = '/bookings/?date=' + date
    fetch(url)
    .then(r => r.json())
    .then(data => {
        handleFetchBookings(data)
    })
}

function handleFetchBookings(data)
{
    bookings_options = ""
    reserved_slots = []

    for(var i = 0; i < data.length; i++)
    {
        var item = data[i]
        reserved_slots.push(item.slot)
        bookings_options += `<p>${item.name} - ${formatTime(item.slot)}</p>`
    }

    slot_options = '<option value="0" disabled>Select time</option>'
    for(var i = 10; i < 20; i++ )
    {
        const label = formatTime(i)
        if(reserved_slots.includes(i))
        {
            slot_options += `<option value=${i} disabled>${label}</option>`
        }
        else
        {
            slot_options += `<option value=${i}>${label}</option>`
        }
    }
    document.getElementById('reservation_slot').innerHTML = slot_options

    if (bookings_options == "")
    {
        bookings_options = "No bookings"
    }
    document.getElementById('bookings').innerHTML = bookings_options
}

function RegisterReserveButton()
{
    document.getElementById('button').addEventListener('click',
    function(e){
        onClickReserveButton()
    })
}

function onClickReserveButton()
{
    let first_name = document.getElementById('first_name').value
    if (first_name == "")
    {
        alert("Please Enter Your Name")
        return
    }
    const form_data = {
      name: first_name,
      no_of_guests: document.getElementById('no_of_guests').value,
      date: document.getElementById('reservation_date').value,
      slot: document.getElementById('reservation_slot').value,
    }
    console.log(form_data)

    fetch(bookUrl, { 
        method: 'post', 
        headers:{
            "Content-type":"application/json",
        },
        body: JSON.stringify(form_data)})
    .then(r => r.json())
    .then( data => {
        console.log("data = " + data)
        handleFetchBookings(data)
    })
}

InitNumberGuestsOptions()
setReservationDate()
RegisterReserveButton()
