from flask import Blueprint, render_template, request

from myutilities.pdf_converts import pdf_tables_to_dataframe, multiple_dfs


bp = Blueprint("drag_n_drop", __name__, template_folder="templates")


@bp.route('/', methods=['GET', 'POST'])
def uploads():
    """:returns HTML"""
    if request.method == 'POST':
        
        # Get the uploaded file name
        f = request.files.get('file')

        # f.save(secure_filename(f.filename))
      
        # Get list of tables in formate of pandas dataframes
        dataframe_list = pdf_tables_to_dataframe(f)
        
        # # Write to Excel and open file
        # write_to_excel(f, dataframe_list)

        out_file_name = (f.filename.split('.')[0] + '.xlsx')
        out_file_name = out_file_name.replace(" ","_")
    
        path = out_file_name
        
        multiple_dfs(dataframe_list, path, 1)

        return render_template('drag_n_drop/index.html')
    
    return render_template('drag_n_drop/index.html')
