fetch ('https://mrkoisp1fg.execute-api.us-east-1.amazonaws.com/prod/empl?id=b3bd3c8b-4bf3-4d09-ba7d-48c5322b62fa', {
    method: 'GET'
}).then(res => res.json())
    .then(res => {
        console.log(res)
    })