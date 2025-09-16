import { Request } from '@/service/request';

describe('Request class', () => {

    let request;

    beforeEach(() => {
        request = new Request();
    });

    it('deve adicionar headers com addHeaders', () => {
        const headers = { 'Content-Type': 'application/json' };
        const result = request.addHeaders(headers, 'X-Test', '123');

        expect(result).toEqual({
        'Content-Type': 'application/json',
        'X-Test': '123',
        });
    });

    it('deve adicionar headers com bearer Authorization', () => {
        const headers = { 'Content-Type': 'application/json' };
        const result = request.withAuth(headers);

        expect(result['Authorization']).toEqual(expect.stringContaining('Bearer'));

    });
    
});