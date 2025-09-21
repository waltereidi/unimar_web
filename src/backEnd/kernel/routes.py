
import os;
class RouteRegister:

    # Importar e registrar blueprints das rotas
    @staticmethod
    def register_blueprints(app):
        """Registra todos os blueprints da pasta routes"""
        routes_path = os.path.join('/src', 'backEnd', 'controllers')
    
        # Função para registrar automaticamente novos blueprints
        def auto_register_blueprints(app):
            """Registra automaticamente todos os blueprints encontrados na pasta routes"""
            import importlib
            import pkgutil
            
            try:
                # Importar o módulo routes
                routes_module = importlib.import_module('backEnd.controllers')
                
                # Procurar por blueprints em todos os módulos da pasta routes
                for _, module_name, _ in pkgutil.iter_modules([routes_path]):
                    if module_name != '__init__':
                        try:
                            module = importlib.import_module(f'backEnd.controllers.{module_name}')
                            
                            # Procurar por atributos que terminam com '_bp' (blueprint)
                            for attr_name in dir(module):
                                if attr_name.endswith('_bp'):
                                    blueprint = getattr(module, attr_name)
                                    if hasattr(blueprint, 'name'):
                                        app.register_blueprint(blueprint, url_prefix=f"/api/{blueprint.name}")
                                        print(f"✅ Blueprint '{blueprint.name}' registrado automaticamente")
                        except Exception as e:
                            print(f"⚠️ Erro ao registrar blueprint do módulo '{module_name}': {e}")
            except Exception as e:
                print(f"⚠️ Erro ao registrar blueprints automaticamente: {e}")
        
        # Executar registro automático
        auto_register_blueprints(app)

    # Registrar blueprints