import { Request } from '@/service/request.js'
export class OpenAiRequests extends Request {

    constructor() {
        super();
    }
    
    async requestOpenAi( pergunta )
    {
        var body = { pergunta : pergunta }
        var header = super.getDefaultHeaders(); 
        header = super.withAuth(header);  
        
        var res= await super.post(`/open_ai/GPT5nano_GetResponse` , 
            body , 
            header
        )
        var body = await res.json();
        return body;
    }
}
