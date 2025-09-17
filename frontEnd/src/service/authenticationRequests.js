import { Request } from '@/service/request.js'
import Toast, { POSITION } from "vue-toastification";
export class AuthenticationRequests extends Request {

    constructor() {
        super();
    }

    async loginAuthentication(email , password)
    {
        // const res = await fetch(`${this.API_URL}/login/authentication`, {
        // method: 'POST',
        // headers: { 'Content-Type': 'application/json' },
        // body: JSON.stringify({ email: form.email, password: form.password, remember: form.remember }),
        // })
        var body ={ email: email, password:password };

        var headers = super.getDefaultHeaders();

        var res =  await super.post(`/login/authentication` , 
            body,
            headers
        );
        console.log(res)
        if(res.status === 200  ){
            var body = await res.json();
            
            super.setToken(body.token);
        }else{
            super.clearToken();
        }
        
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




