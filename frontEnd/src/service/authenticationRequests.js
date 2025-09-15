export class AuthenticationRequests {
    constructor() {}
    async loginAuthentication()
    {
        const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000';
        const res = await fetch(`${this.API_URL}/login/authentication`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: form.email, password: form.password, remember: form.remember }),
        })

        return res.json() 
    }

    async validateToken(token)
    {
        const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000';
        const res = await fetch(`${API_URL}/login/validate_token`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' , 
        'Authorization': `Bearer ${token}`
        },
        })

        return res.json() 
    }

}




