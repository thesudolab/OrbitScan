from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, DataTable
from textual.containers import Container
import asyncio

class OrbitScan(App):
    """The main interface for OrbitScan."""
    
    BINDINGS = [("q", "quit", "Quit"), ("s", "scan", "Start Scan")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield DataTable(cursor_type="row")
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns("Service", "Resource", "Status", "Description")
        table.add_row("System", "Initial", "Ready", "Press 's' to start scan")

    async def action_scan(self) -> None:
        """Triggers the scan process."""
        table = self.query_one(DataTable)
        table.clear()
        
        # Simulated async scan
        table.add_row("S3", "prod-bank-data", "[yellow]Scanning...[/]", "Checking Public Access")
        await asyncio.sleep(2) # Simulate network lag
        table.update_cell("S3", "prod-bank-data", "[green]PASS[/]")
        table.update_cell("S3", "prod-bank-data", "Public Access Blocked", column_index=3)

if __name__ == "__main__":
    app = OrbitScan()
    app.run()