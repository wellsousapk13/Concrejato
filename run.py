import os
from app import create_app, db
from app.models.user import User
from app.models.funcionario import Funcionario

app = create_app()

def init_database():
    """Cria tabelas no banco de dados e popula usuários e dados padrão caso não existam."""
    with app.app_context():
        db.create_all()

        # Migração segura para SQLite (adicionar colunas novas se a tabela já existia antes)
        try:
            with db.engine.connect() as conn:
                result = conn.execute(db.text("PRAGMA table_info(controles_previos)")).fetchall()
                col_names = [r[1] for r in result]
                if 'funcionarios_assinaturas' not in col_names and len(col_names) > 0:
                    conn.execute(db.text("ALTER TABLE controles_previos ADD COLUMN funcionarios_assinaturas JSON"))
                    conn.commit()
                    print("[DB MIGRATION] Coluna 'funcionarios_assinaturas' adicionada à tabela controles_previos.")
        except Exception as e:
            print(f"[DB MIGRATION NOTE] {e}")

        # Criar Administrador padrão se não existir
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            admin = User(
                username='admin',
                nome_completo='Administrador do Sistema',
                email='admin@empresa.com',
                role='ADMIN',
                ativo=True
            )
            admin.set_password('admin123')
            db.session.add(admin)
            print("[DB INIT] Usuário Administrador criado (admin / admin123)")

        # Criar Operador padrão se não existir
        operador = User.query.filter_by(username='operador').first()
        if not operador:
            operador = User(
                username='operador',
                nome_completo='Operador de Campo',
                email='operador@empresa.com',
                role='OPERADOR',
                ativo=True
            )
            operador.set_password('operador123')
            db.session.add(operador)
            print("[DB INIT] Usuário Operador criado (operador / operador123)")

        # Cadastrar alguns funcionários padrão para teste rápido se não houver nenhum
        if Funcionario.query.count() == 0:
            f1 = Funcionario(nome='João da Silva', cpf_matricula='MAT-101', funcao='Eletricista', empresa='CONCREJATO ENGENHARIA')
            f2 = Funcionario(nome='Carlos Oliveira', cpf_matricula='MAT-102', funcao='Encarregado', empresa='CONCREJATO ENGENHARIA')
            f3 = Funcionario(nome='Pedro Santos', cpf_matricula='MAT-103', funcao='Ajudante', empresa='CONCREJATO ENGENHARIA')
            db.session.add_all([f1, f2, f3])
            print("[DB INIT] Funcionários padrão cadastrados.")

        db.session.commit()


# Inicializa o banco automaticamente tanto via WSGI/Gunicorn (nuvem) quanto em execução direta
try:
    init_database()
except Exception as e:
    print(f"[DB INIT WARNING] {e}")


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_DEBUG', '0').lower() in ('1', 'true', 'yes')
    print(f"\n=======================================================")
    print(f" SISTEMA DIGITAL DE RELATÓRIOS EMPRESARIAIS - CONCREJATO")
    print(f" Servidor iniciado em: http://0.0.0.0:{port}")
    print(f" Usuário Admin: admin / admin123")
    print(f" Usuário Operador: operador / operador123")
    print(f"=======================================================\n")
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
