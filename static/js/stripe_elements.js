var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var element = stripe.elements();

var style = {
    base: {
        color: '#313232',
        fontFamily: '"Be Vietnam Pro", Be Vietnam Pro, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#313232'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

var card = element.create('card', {style: style});
card.mount('#card-element');
