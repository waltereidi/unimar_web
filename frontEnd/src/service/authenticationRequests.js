import { Request } from '@/service/request.js'

export class AuthenticationRequests extends Request {

    constructor() {
        super();
    }

    async loginAuthentication()
    {
        // const res = await fetch(`${this.API_URL}/login/authentication`, {
        // method: 'POST',
        // headers: { 'Content-Type': 'application/json' },
        // body: JSON.stringify({ email: form.email, password: form.password, remember: form.remember }),
        // })

        var res = super.post(`/login/authentication` , 
            JSON.stringify({ email: form.email, password: form.password, remember: form.remember }),
            super.getDefaultHeaders()
        )
        return res

    }

    async validateToken(token = "")
    {
        // const res = await fetch(`${API_URL}/login/validate_token`, {
        // method: 'POST',
        // headers: { 'Content-Type': 'application/json' , 
        // 'Authorization': `Bearer ${token}`
        // },
        // })
        // return res
        var header = super.getDefaultHeaders()
        header = super.withAuth(header)
        var res = super.post(`/login/validate_token`, 
            null , 
            header
        )

        return res
    }

}




