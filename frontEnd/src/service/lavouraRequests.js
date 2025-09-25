import { Request } from '@/service/request.js'
export class LavouraRequests extends Request {

    constructor() {
        super();
    }

    async getRendimentoPonderadoUf( ano )
    {
        var body = { ano : ano };
        var headers = super.getDefaultHeaders();
        headers = super.withAuth(headers);

        var res =await super.post(`/lavoura_permanente/rendimento_ponderado_por_uf`,
            body , 
            headers
         );
        
        var body = await res.json();
        return body;            
    }
    async getIndicadoresAgricolas( ano )
    {
        var body = { ano : ano }
        var header = super.getDefaultHeaders(); 
        header = super.withAuth(header);  

        var res= await super.post(`/lavoura_permanente/indicadores_agricolas` , 
            body , 
            header
        )
        var body = await res.json();
        return body;
    }
        async requestOpenAi( pergunta )
    {
        var body = { pergunta : pergunta }
        var header = super.getDefaultHeaders(); 
        header = super.withAuth(header);  
        console.log("openAi")
        var res= await super.post(`/open_ai/GPT5nano_GetResponse` , 
            body , 
            header
        )
        var body = await res.json();
        return body;
    }

}